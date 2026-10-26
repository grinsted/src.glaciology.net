"""Collect attribution evidence for page banner images.

Usage (from the repo root):
    python scripts/python/banner_credits.py scan [out.csv]
    python scripts/python/banner_credits.py apply [in.csv]

scan writes one row per page with a banner and no banner_credit. Evidence comes
from image metadata (JPEG comment, EXIF, XMP), the filename, Wikimedia Commons
(by source URL, filename and SHA1) and credit-like text in the page body.
Review the CSV and mark rows with approved=y before applying them.

apply adds banner_credit (from the banner_credit column) to every approved page
that does not already have one, as a new line right after the banner line.
"""

import csv
import hashlib
import html
import json
import os
import re
import sys
import time
import tomllib
import urllib.parse
import urllib.request

import io

import yaml
from PIL import Image, ImageOps

CONTENT = "content"
STATIC = "static"
COMMONS_API = "https://commons.wikimedia.org/w/api.php"
USER_AGENT = "glaciology.net banner-credit scan (https://www.glaciology.net)"

FRONTMATTER = re.compile(r"\A(---|\+\+\+)\s*\n(.*?)\n\1\s*\n", re.DOTALL)
COMMONS_URL = re.compile(r"commons\.wikimedia\.org/wiki/(File:[^\s\"'<>]+)", re.I)
URL = re.compile(r"https?://[^\s\"'<>)\]]+")
FLICKR_ID = re.compile(r"^(\d{8,11})_[0-9a-f]{10}(?:_[a-z0-9])?$")
CREDIT_IN_NAME = re.compile(r"credit[-_ ]+(.+)$", re.I)
NASA_NAME = re.compile(r"(^iss\d{3}e\d+|nasa|icebridge|landsat|modis)", re.I)
AI_NAME = re.compile(r"(ai[-_ ]?generated|dall-?e|midjourney|stable[-_ ]?diffusion)", re.I)
BODY_HINT = re.compile(
    r"wikimedia|wikipedia|creative ?commons|cc[- ]by|unsplash|flickr|courtesy|"
    r"image (credit|source|from)|photo(graph)? (by|credit)|credit:",
    re.I,
)
XMP_FIELDS = ["dc:creator", "dc:rights", "photoshop:Credit", "photoshop:Source",
              "xmpRights:WebStatement", "cc:license", "dc:source"]
JUNK_VALUES = {"", "unknown", "picasa", "copyright 2006"}
SAME_IMAGE_DISTANCE = 12  # max dHash bit difference (of 64) to call two images the same


def read_page(path):
    text = open(path, encoding="utf8", errors="ignore").read()
    m = FRONTMATTER.match(text)
    if not m:
        return None, text
    try:
        meta = yaml.safe_load(m.group(2)) if m.group(1) == "---" else tomllib.loads(m.group(2))
    except Exception as e:
        print(f"  could not parse front matter in {path}: {e}")
        return None, text
    return meta or {}, text[m.end():]


def find_image(banner, page):
    rel = urllib.parse.unquote(banner)
    if rel.startswith("http"):
        return None
    candidates = [os.path.join(os.path.dirname(page), rel)] if not rel.startswith("/") else []
    candidates += [os.path.join(STATIC, rel.lstrip("/")), os.path.join(CONTENT, rel.lstrip("/"))]
    return next((c for c in candidates if os.path.isfile(c)), None)


def xmp_value(xmp, field):
    attr = re.search(rf'{field}="([^"]*)"', xmp)
    if attr:
        return attr.group(1)
    elem = re.search(rf"<{field}\b[^>]*?(?:rdf:resource=\"([^\"]*)\")?[^>]*>(.*?)</{field}>", xmp, re.S)
    if elem:
        return elem.group(1) or re.sub(r"\s+", " ", re.sub(r"<[^>]+>", " ", elem.group(2))).strip()
    return None


def image_metadata(path):
    """Return a dict of credit-relevant metadata found in the image file."""
    found = {}
    try:
        im = Image.open(path)
    except Exception as e:
        return {"error": str(e)}
    comment = im.info.get("comment")
    if isinstance(comment, bytes):
        comment = comment.decode("utf8", "ignore")
    if comment and "CREATOR: gd-jpeg" not in comment:
        found["comment"] = comment.strip()
    exif = im.getexif()
    for tag, name in [(315, "exif_artist"), (33432, "exif_copyright"), (270, "exif_description")]:
        value = str(exif.get(tag, "")).strip()
        if value.lower() not in JUNK_VALUES:
            found[name] = value
    xmp = im.info.get("xmp") or im.info.get("XML:com.adobe.xmp")
    if isinstance(xmp, bytes):
        xmp = xmp.decode("utf8", "ignore")
    for field in XMP_FIELDS if xmp else []:
        value = xmp_value(xmp, field)
        if value and value.lower() not in JUNK_VALUES:
            found["xmp_" + field.split(":")[1].lower()] = html.unescape(value)
    return found


def commons_get(**params):
    params.update(action="query", format="json", formatversion=2)
    url = COMMONS_API + "?" + urllib.parse.urlencode(params)
    req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    time.sleep(0.2)
    with urllib.request.urlopen(req, timeout=30) as r:
        return json.load(r)["query"]


def commons_info(titles):
    """Look up Commons file pages; returns {requested title: info} for files that exist."""
    found = {}
    titles = list(dict.fromkeys(titles))
    for i in range(0, len(titles), 50):
        chunk = titles[i:i + 50]
        q = commons_get(titles="|".join(chunk), redirects=1, prop="imageinfo",
                        iiprop="url|sha1|extmetadata", iiurlwidth=256, iiextmetadatafilter="Artist|LicenseShortName|LicenseUrl|Credit")
        alias = {t: t for t in chunk}
        for n in q.get("normalized", []) + q.get("redirects", []):
            for k, v in list(alias.items()):
                if v == n["from"]:
                    alias[k] = n["to"]
        pages = {p["title"]: p for p in q.get("pages", []) if not p.get("missing") and p.get("imageinfo")}
        for t, canonical in alias.items():
            if canonical in pages:
                found[t] = pages[canonical]
    return found


def commons_by_sha1(sha1):
    try:
        hits = commons_get(list="allimages", aisha1=sha1, ailimit=1).get("allimages", [])
    except Exception:
        return None
    return hits[0]["title"] if hits else None


def dhash(im):
    g = ImageOps.exif_transpose(im).convert("L").resize((9, 8), Image.LANCZOS)
    px = list(g.getdata())
    return sum(1 << i for i in range(64) if px[i // 8 * 9 + i % 8] > px[i // 8 * 9 + i % 8 + 1])


def looks_same(local_path, thumb_url):
    """Compare a local image with a Commons thumbnail; returns the dHash distance or None."""
    try:
        req = urllib.request.Request(thumb_url, headers={"User-Agent": USER_AGENT})
        with urllib.request.urlopen(req, timeout=30) as r:
            remote = Image.open(io.BytesIO(r.read()))
        return bin(dhash(Image.open(local_path)) ^ dhash(remote)).count("1")
    except Exception:
        return None


def html_to_markdown(s):
    s = re.sub(r'<a [^>]*href="[^"]*redlink=1[^"]*"[^>]*>(.*?)</a>', r"\1", s, flags=re.S)
    s = re.sub(r'<a [^>]*href="([^"]+)"[^>]*>(.*?)</a>',
               lambda m: f"[{re.sub(r'<[^>]+>', '', m.group(2)).strip()}]({m.group(1)})", s, flags=re.S)
    s = re.sub(r"<[^>]+>", "", s)
    s = re.sub(r"\]\(//", "](https://", s)
    return re.sub(r"\s+", " ", html.unescape(s)).strip()


def commons_credit(page):
    ii = page["imageinfo"][0]
    meta = ii.get("extmetadata", {})
    artist = html_to_markdown(meta.get("Artist", {}).get("value", "")) or "Unknown author"
    artist = re.sub(r"^Image:?\s*", "", artist)
    lic = meta.get("LicenseShortName", {}).get("value", "")
    lic_url = meta.get("LicenseUrl", {}).get("value", "")
    lic_md = f"[{lic}]({lic_url})" if lic_url else (lic or "license unknown")
    return f"Image: {artist}, {lic_md}, via [Wikimedia Commons]({ii['descriptionurl']})", ii["descriptionurl"], ii["sha1"]


def body_hints(body):
    hints = []
    for line in body.splitlines():
        if BODY_HINT.search(line):
            hints.append(line.strip()[:200])
    return hints


def scan(out_path):
    rows = []
    for root, _, files in os.walk(CONTENT):
        for f in sorted(files):
            if not f.endswith(".md"):
                continue
            page = os.path.join(root, f)
            meta, body = read_page(page)
            if not meta or not meta.get("banner") or meta.get("banner_credit"):
                continue
            banner = str(meta["banner"])
            image = find_image(banner, page)
            stem = os.path.splitext(os.path.basename(urllib.parse.unquote(banner)))[0]
            row = dict(page=page, banner=banner, image=image, image_found="yes" if image else "no",
                       confidence="none", category="", suggested_credit="", source_url="",
                       evidence=[], commons_titles=[], sha1="")
            if image:
                md = image_metadata(image)
                row["evidence"] += [f"{k}: {v}" for k, v in md.items()]
                row["sha1"] = hashlib.sha1(open(image, "rb").read()).hexdigest()
                for v in md.values():
                    row["commons_titles"] += [urllib.parse.unquote(t) for t in COMMONS_URL.findall(v)]
                    if not row["source_url"]:
                        urls = URL.findall(v)
                        row["source_url"] = urls[0] if urls else ""
                if md.get("xmp_creator") or md.get("exif_artist"):
                    creator = md.get("xmp_creator") or md.get("exif_artist")
                    rights = md.get("xmp_rights") or md.get("exif_copyright") or ""
                    row.update(confidence="medium", category="image metadata",
                               suggested_credit=f"Image: {creator}" + (f" ({rights})" if rights and rights not in creator else ""))
            row["commons_titles"].append("File:" + os.path.basename(urllib.parse.unquote(banner)))

            if m := CREDIT_IN_NAME.search(stem):
                name = re.sub(r"[-_]+", " ", m.group(1)).strip()
                row["evidence"].append(f"filename credit: {name}")
                if row["confidence"] == "none":
                    row.update(confidence="medium", category="filename", suggested_credit=f"Credit: {name}")
            if m := FLICKR_ID.match(stem):
                url = f"https://www.flickr.com/photo.gne?id={m.group(1)}"
                row["evidence"].append(f"flickr id: {url}")
                if row["confidence"] == "none":
                    row.update(confidence="low", category="flickr", source_url=url)
            if NASA_NAME.search(stem):
                row["evidence"].append("filename suggests NASA/US government imagery")
                if row["confidence"] == "none":
                    row.update(confidence="low", category="nasa", suggested_credit="Credit: NASA")
            if AI_NAME.search(stem):
                row["evidence"].append("filename suggests AI-generated image")
                if row["confidence"] == "none":
                    row.update(confidence="low", category="ai-generated", suggested_credit="AI-generated image")
            hints = body_hints(body)
            row["evidence"] += [f"page text: {h}" for h in hints]
            if hints and row["confidence"] == "none":
                row.update(confidence="low", category="page text")
            rows.append(row)
            print(f"{len(rows):4d} {page}")

    print("Querying Wikimedia Commons by filename ...")
    info = commons_info([t for r in rows for t in r["commons_titles"]])
    print("Querying Wikimedia Commons by SHA1 ...")
    for row in rows:
        title = next((t for t in row["commons_titles"] if t in info), None)
        exact = False
        if not title and row["sha1"]:
            sha_title = commons_by_sha1(row["sha1"])
            if sha_title:
                info.update(commons_info([sha_title]))
                title, exact = sha_title, True
        if title and title in info:
            credit, url, sha1 = commons_credit(info[title])
            exact = exact or sha1 == row["sha1"]
            explicit = title in row["commons_titles"][:-1]
            dist = None if exact or not row["image"] else looks_same(row["image"], info[title]["imageinfo"][0].get("thumburl", ""))
            if exact:
                how, confidence = "identical file", "high"
            elif dist is not None and dist <= SAME_IMAGE_DISTANCE:
                how, confidence = f"name match, looks the same (dhash {dist})", "high"
            elif explicit:
                how, confidence = f"source named in image metadata (dhash {dist})", "medium"
            else:
                row["evidence"].insert(0, f"commons: {title} has the same name but looks different (dhash {dist}): {url}")
                continue
            row["evidence"].insert(0, f"commons: {title} ({how})")
            row.update(suggested_credit=credit, source_url=url, category="wikimedia commons", confidence=confidence)
        if not row["category"] and row["page"].startswith(os.path.join(CONTENT, "publication")):
            row["category"] = "publication (own figure?)"

    order = {"high": 0, "medium": 1, "low": 2, "none": 3}
    rows.sort(key=lambda r: (order[r["confidence"]], r["page"]))
    fields = ["page", "banner", "image_found", "confidence", "category", "suggested_credit",
              "banner_credit", "approved", "source_url", "evidence"]
    with open(out_path, "w", newline="", encoding="utf8") as fh:
        w = csv.DictWriter(fh, fieldnames=fields, extrasaction="ignore")
        w.writeheader()
        for r in rows:
            w.writerow({**r, "banner_credit": r["suggested_credit"], "approved": "",
                        "evidence": " | ".join(r["evidence"])})

    counts = {}
    for r in rows:
        counts[r["confidence"]] = counts.get(r["confidence"], 0) + 1
    print(f"\nWrote {len(rows)} rows to {out_path}")
    for c in order:
        print(f"  {c:7s} {counts.get(c, 0)}")


def credit_line(credit, toml):
    if toml:
        return f"banner_credit = {json.dumps(credit, ensure_ascii=False)}"
    return yaml.safe_dump({"banner_credit": credit}, allow_unicode=True, width=10**6).strip()


def apply(in_path):
    with open(in_path, newline="", encoding="utf8") as fh:
        rows = list(csv.DictReader(fh))
    applied, unchanged, skipped = 0, 0, []
    for row in rows:
        if row.get("approved", "").strip().lower() not in ("y", "yes"):
            continue
        page = row["page"].strip()
        credit = re.sub(r"\s+", " ", row.get("banner_credit", "")).strip()
        if not credit:
            skipped.append((page, "empty banner_credit"))
            continue
        if not os.path.isfile(page):
            skipped.append((page, "page not found"))
            continue
        meta, _ = read_page(page)
        if meta is None:
            skipped.append((page, "no front matter"))
            continue
        if meta.get("banner_credit") == credit:
            unchanged += 1
            continue
        if meta.get("banner_credit"):
            skipped.append((page, f"already has a different banner_credit: {meta['banner_credit']}"))
            continue
        text = open(page, encoding="utf8").read()
        toml = text.startswith("+++")
        fm = FRONTMATTER.match(text)
        banner = re.search(r"^banner\s*[:=].*$", fm.group(2), re.M)
        if not banner:
            skipped.append((page, "no banner line in front matter"))
            continue
        pos = fm.start(2) + banner.end()
        new = text[:pos] + "\n" + credit_line(credit, toml) + text[pos:]
        with open(page, "w", encoding="utf8", newline="") as fh:
            fh.write(new)
        meta, _ = read_page(page)
        if not meta or meta.get("banner_credit") != credit or str(meta.get("banner")) != row["banner"]:
            with open(page, "w", encoding="utf8", newline="") as fh:
                fh.write(text)
            skipped.append((page, "front matter did not round-trip; left unchanged"))
            continue
        applied += 1
    print(f"Added banner_credit to {applied} pages ({unchanged} already up to date)")
    for page, why in skipped:
        print(f"  skipped {page}: {why}")


if __name__ == "__main__":
    commands = {"scan": scan, "apply": apply}
    if len(sys.argv) < 2 or sys.argv[1] not in commands:
        sys.exit(__doc__)
    commands[sys.argv[1]](sys.argv[2] if len(sys.argv) > 2 else "banner_credits.csv")

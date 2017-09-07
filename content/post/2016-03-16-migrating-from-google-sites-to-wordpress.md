---
title: Migrating from Google Sites to WordPress
date: 2016-03-16T08:37:16+00:00
author: aslak
banner: /2016/03/AlphabetPasta.jpg
tags:
  - Tip
aliases:
  - /2016/03/16/migrating-from-google-sites-to-wordpress/
---
I recently migrated from google sites to wordpress. There is lots to like about google sites (high uptime, zero maintenance), and I have been quite happy there. The primary reasons for my move are: I have a server anyway, and I would like to allow comments on some of my posts. I could not find any tools that allowed me export & import google sites. I tried importing from the RSS feed, but eventually I found a much better option: python (I don't do much programming in python, but it is really a pleasure to work in for these types of tasks).

# First pass

  * Parse and traverse my google-sites pages (using beautifulsoup).
  * Clean the html of the main content using regexps.
  * Find all images in content. Download them to a local file.
  * Upload images to wordpress using [python-wordpress-xmlrpc](https://python-wordpress-xmlrpc.readthedocs.org/en/latest/ref/wordpress.html), and replace image urls in content html.
  * Create new posts using [python-wordpress-xmlrpc](https://python-wordpress-xmlrpc.readthedocs.org/en/latest/ref/wordpress.html) . In this pass you should aim to set the content, the title, the date,  (I used dateutil.parser to set the date of the post)

# Second pass

All the internal links on the new site are still pointing to the old site. I fixed this in a second pass.

  * Get a list of all posts using the XMLRPC. From that make a list of all the post titles.
  * Loop each post, and for each url pointing to the old site, try to see if the [basename](https://docs.python.org/2/library/os.path.html) has a close match in the list of wordpress titles. For that I used [difflib.get\_close\_matches](https://docs.python.org/2/library/difflib.html#difflib.get_close_matches).



I did not find a way to automatically download non-image google sites attachments (such as pdfs). Google appears to deliberately have made that difficult. I did not investigate further.

I'd love to share my code. Unfortunately I had to go through a learning process and my approach was not nearly as clean as outlined above. So you'll have to make do with snippets to get you started. I am not a python programmer, so please excuse the style:



```python
from bs4 import BeautifulSoup
import requests
import re
import shutil
from wordpress_xmlrpc import Client, WordPressPost
from wordpress_xmlrpc.compat import xmlrpc_client
from wordpress_xmlrpc.methods import media, posts
from urlparse import urlparse
from os.path import splitext, basename
from glob import glob
from difflib import get_close_matches
from dateutil import parser
import mimetypes
mimetypes.init()
wpUserName='username'
wpPassword='password'
wpUrl='http://blog.example.com/xmlrpc.php'
client = Client(wpUrl,wpUserName,wpPassword)
allposts=client.call(posts.GetPosts({'number':1000}))
posttitles=[post.title for post in allposts]
for post in allposts:
    print "-------------------------"
    print repr(post.title)
    txt=unicode(post.content)
    links=re.findall(r'href="[^>"]*google-sites.example.com[^>"]*/([^>"\?]*)', txt)
    for link in links:
        titlematches=get_close_matches(link,posttitles)
        if titlematches:
            matchingpost = next((i for i in allposts if i.title == titlematches[0]), None)
            txt=re.sub(r'"[^>\n"]*' + re.escape(link) + r'[^>\n"]*"','"'+ matchingpost.link +'"',txt)
            print repr(link) + " -> " + repr(matchingpost.link)
        else:
            print "NO MATCH FOR LINK:" + repr(link)
    post.content=re.sub(r"https?://blog.example.com/","/",txt);
    client.call(posts.EditPost(post.id,post))
```

update: I have since decided to migrate to a static website generator: Hugo.  

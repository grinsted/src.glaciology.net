---
title: Compiling multiple markdown files to epub
date: 2025-08-25 05:24:00+00:00
author: aslak
banner: /post/2025/obsidian-credit-james-st-john.jpg
---

I've been experimenting with different ways of converting a whole folder of obsidian markdown files to epub using pandoc. Here are some different options that I've explored. 

The [longform plugin](https://github.com/kevboh/longform) is probably the go to option, but it comes with a workflow that doesn't suit me. So I abandoned that for my little project.

The [include-files.lua](https://github.com/pandoc-ext/include-files) filter for pandoc. This might be the cleanest solution - you can just add it as an option in the standard obsidian exporter. But you might need some additional magic if you want to resolve wikilinks to images. 

So i ended up using a custom python script that compiles a long command line for pandoc. It adds all the md files to the command line, sorts them, and adds all the folders . This will also resolve wikilinks by recursively adding a bunch of resource folders. 

```python
import glob
import re
import subprocess
import os

natsortkey = lambda s: [int(t) if t.isdigit() else t.lower() for t in re.split(r'(\d+)', s)]

natsort = lambda L: sorted(L, key=natsortkey)
  
files = glob.glob("manuscript/**/*.md",recursive=True)
files= natsort(files)

# To resolve wikilinks you need to add a list of search paths
resource_folders = glob.glob("**/",recursive=True)
resource_folders = ['.']+[os.path.abspath(f) for f in resource_folders]

cmd = ["pandoc", "-o", "Frankenstein.epub",
       "-B", "Titlepage.html",
       "--toc", "--css", "epub.css",
       "--resource-path", ';'.join(resource_folders), 
       "--embed-resources",
       "--from=markdown+wikilinks_title_after_pipe",
       "--epub-title-page=false",
       "--metadata","title=Frankenstein",
       ] +files

result = subprocess.run(cmd,capture_output = True, text = True )

print(result.stdout)
print(result.stderr)
```


Other alternatives considered:
* The Easy Bake obsidian plugin - but it seems abandoned and i did not get it to work (but also gave up fast because i really dont want to bake it). 
* A shell script that does the same as the python script above. 
* A custom pandoc lua filter that does something similar. 
* Using the obsidian RunJS plugin to achieve something similar. It seemed to big effort to learn.











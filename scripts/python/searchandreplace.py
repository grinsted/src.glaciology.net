import requests

#var = requests.get(r'http://www.google.com/search?q="SEA LEVEL RISE PROJECTIONS FOR NORTHERN EUROPE UNDER RCP8.5+site:https://www.glaciology.net"&btnI')
#print var.url

import os, re
import sys
import time
import urllib

#cleanre = re.compile(r'^layout:[^\n]*\n', re.MULTILINE |re.DOTALL)
cleanre = re.compile(r'^categories:[^\n]*\n\s*-[^\n]*\n', re.MULTILINE |re.DOTALL)


# traverse root directory, and list directories as dirs and files as files
for root, dirs, files in os.walk("content"):
    for file in files:
        if file.endswith('.md'):
            print(file)
            file=os.path.join(root, file)
            with open(file, 'r', encoding='utf8', errors='ignore') as content_file:
                content = content_file.read()

            content = re.sub(cleanre,'',content)
            #print(content)
            #sys.exit(' ')

            with open(file, 'w',encoding='utf-8',errors='ignore') as content_file:
                content_file.write(content)

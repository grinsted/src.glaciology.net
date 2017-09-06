import requests

#var = requests.get(r'http://www.google.com/search?q="SEA LEVEL RISE PROJECTIONS FOR NORTHERN EUROPE UNDER RCP8.5+site:https://www.glaciology.net"&btnI')
#print var.url

import os, re
import sys
import time
import urllib

cleanre = re.compile(r'^layout:[^\n]*\n', re.MULTILINE |re.DOTALL)



# traverse root directory, and list directories as dirs and files as files
for root, dirs, files in os.walk("../../content"):
    for file in files:
        if file.endswith('.md'):
            print(file)
            file=os.path.join(root, file)
            with open(file, 'rb') as content_file:
                content = content_file.read().decode('utf8', 'ignore')
            #searchObj = re.search( r'^\s*title: (.*)', content, re.M|re.I)
            #title = searchObj.group(1)
            #print(title)

            #print(content)
            if True:
                content = re.sub(cleanre,'',content)
                #if content.find('permalink')<0:
                #    print 'No permalink'
                #    continue
                #content = re.sub(permalinktoalias,'---\\1\\3\n  - \\2',content)
                #print(content)

            #sys.exit(' ')
            with open(file, 'w',encoding='utf-8') as content_file:
                content_file.write(content)

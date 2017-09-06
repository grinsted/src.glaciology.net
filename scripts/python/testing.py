import requests

#var = requests.get(r'http://www.google.com/search?q="SEA LEVEL RISE PROJECTIONS FOR NORTHERN EUROPE UNDER RCP8.5+site:https://www.glaciology.net"&btnI')
#print var.url



import os, re
import sys
import time
import urllib

headerre = re.compile(r'^\s*---(.*)---\s*$', re.MULTILINE |re.DOTALL)

failedre = re.compile(r'^\s*---(.*)aliases:.*format=json.*---\s*$', re.MULTILINE |re.DOTALL)

cleanre = re.compile(r'interface_sidebarlayout:\s*- default\s*', re.MULTILINE |re.DOTALL)



# traverse root directory, and list directories as dirs and files as files
for root, dirs, files in os.walk("../../content"):
    for file in files:
        if file.endswith('.md'):
	    	file=os.path.join(root, file)
        	with open(file, 'r') as content_file:
        		content = content_file.read()
			searchObj = re.search( r'^\s*title: (.*)', content, re.M|re.I)
			title = searchObj.group(1)
			#var = requests.get(r'http://www.google.com/search?q="%22{}%22+site:https://www.glaciology.net"&btnI'.format(title))
			#aliasurl = var.url



			print title

			if False:
				if content.find('aliases:')>=0:
					continue
				var = requests.get(r'https://api.duckduckgo.com/?q=%5C{}+site:www.glaciology.net&format=json'.format(urllib.quote(title)))
				aliasurl = var.url

				if aliasurl.find('glaciology.net')<0:
					print 'No alias'
					continue
				if aliasurl.find('misc-debris-list')>=0:
					print 'No alias'
					continue
				if aliasurl.find('format=json')>=0:
					print 'No alias'
					continue
				aliasurl = re.sub('.*?glaciology.net','',aliasurl)

				print aliasurl

				content = re.sub(headerre,'---\\1aliases:\n  - {}\n---'.format(aliasurl),content)
				print content
			else:
				#content = re.sub(failedre,'---\\1---',content)
				content = re.sub(cleanre,'',content)
				#if content.find('permalink')<0:
				#	print 'No permalink'
				#	continue
				#content = re.sub(permalinktoalias,'---\\1\\3\n  - \\2',content)
				print content

			sys.exit(' ')
        	with open(file, 'w') as content_file:
        		content_file.write(content)

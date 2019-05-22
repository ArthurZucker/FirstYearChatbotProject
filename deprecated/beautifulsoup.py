#!/usr/bin/env python3

import requests
from bs4 import BeautifulSoup

# utf-8 encoding
url = "https://gameofthrones.fandom.com/wiki/Jon_Snow"
cookies = dict(BCPermissionLevel='PERSONAL')
html = requests.get(url, cookies=cookies, headers={'User-agent':'Mozilla/5.0'})
#r.encoding = 'ISO-8859-1'
#If request == 200
soup = BeautifulSoup(html.content,"html.parser")
# print(html.text)
soup.prettify("latin-1")
soup.encode("ascii","replace")
# kill all script and style elements
for script in soup(["script", "style"]):
    script.extract()    # rip it out

# get text
text = soup.get_text()
# break into lines and remove leading and trailing space on each
lines = (line.strip() for line in text.splitlines())
# break multi-headlines into a line each
chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
# drop blank lines
text = '\n'.join(chunk for chunk in chunks if chunk)
# print(text)
for c in text:
	if ord(c) > 127:
		text = text.replace(c, u'')
		pass

f = open("parseddata.txt","w")
f.write(text)
f.close()

#!/usr/bin/env python3

import requests
from bs4 import BeautifulSoup

# utf-8 encoding
url = "https://awoiaf.westeros.org/index.php/Arya_Stark"
cookies = dict(BCPermissionLevel='PERSONAL')
html = requests.get(url, cookies=cookies, headers={'User-agent':'Mozilla/5.0'})
soup = BeautifulSoup(html.content,"html.parser")
for c in text:
	if ord(c) > 127:
		text = text.replace(c, u'')
		pass
def cleaning_text3(text):
	text_cleaned = ''
	Li = []
	for i in range(len(text)):
		#print(words)
		if i < len(text)-8 and text[i:i+8] == 'Season 8' and len(Li) == 0:
			#cpt = cpt+1
			Li.append(i)
			#print("HEY")
			pass
		elif i < len(text)-8 and text[i:i+8] == 'Contents' and len(Li) == 1:
			Li.append(i)
			pass
		if len(Li) == 2:
			text_cleaned = text[Li[0]+9:Li[1]-1]
			return text_cleaned
	return text_cleaned

#print(cleaning_text(text))
print(cleaning_text(text))


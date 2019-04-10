# utf-8 encoding

import urllib
from bs4 import BeautifulSoup

dic = {'a':10, 'b':11, 'c':12, 'd':13, 'e':14, 'f':15}

url = "https://www.imdb.com/title/tt0113540/"
html = urllib.urlopen(url).read()
print(html)
soup = BeautifulSoup(html)
soup.prettify("latin-1")
soup.encode("ascii")
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
print(text)
for c in text:
	if ord(c) > 127:
		text = text.replace(c, u'')
		pass
#text = text.replace(u'\xa0', u' ')
#text = text.replace(u'\xa9', u'')
with open("parseddata.txt", "wb") as logfile:
    logfile.write(text)

# utf-8 encoding

import urllib
from bs4 import BeautifulSoup

url = "https://www.imdb.com/title/tt0113540/"
html = urllib.urlopen(url).read()
#utiliser request
#import requests
#html = requests.get("https://www.imdb.com/title/tt0113540/")
#html.status_code
print(html)
soup = BeautifulSoup(html)
soup.prettify("latin-1")
soup.encode("ascii")
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
print(text)
text = text.replace(u'\xa0', u' ')
text = text.replace(u'\xa9', u'')
with open("parseddata.txt", "wb") as logfile:
    logfile.write(text)

import urllib
import requests
from bs4 import BeautifulSoup
# utf-8 encoding
url = "https://garden.org/plants/view/533137/Bananas-Musa/"
cookies = dict(BCPermissionLevel='PERSONAL')
html = requests.get(url, cookies=cookies, headers={'User-agent':'Mozilla/5.0'})
#html = urllib.urlopen(url).read()
soup = BeautifulSoup(html.content,"html.parser")
print(html.text)
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
print(text)
text = text.replace(u'\xa0', u' ')
text = text.replace(u'\xa9', u'')
with open("parseddata.txt", "wb") as logfile:
    logfile.write(text)

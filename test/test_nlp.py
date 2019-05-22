import nltk 
import urllib.request

#nltk.download('stopwords')
from nltk.corpus import stopwords
from bs4 import BeautifulSoup

response =  urllib.request.urlopen('https://gameofthrones.fandom.com/wiki/Jon_Snow')
html = response.read()
#print(html)

punctuation = ['-', ',', '.', '?', '=', '/', ':', '+', '1', '2', '3']
soup = BeautifulSoup(html,'lxml')
text = soup.span.get_text()
#tokens = [t for t in text.split()]
print(text)


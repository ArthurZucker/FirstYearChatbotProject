from bs4 import BeautifulSoup
import urllib.request

response =  urllib.request.urlopen('https://gameofthrones.fandom.com/wiki/Jon_Snow')
html = response.read()
#print(html)
punctuation = ['-', ',', '.', '?', '=', '/', ':', '+', '1', '2', '3']
soup = BeautifulSoup(html,'lxml')

with open("parseddata.txt", "wb") as file:
    for link in soup.find_all('img'):
        print(link.get('src'))
        file.write(link.get('src')+"\n")

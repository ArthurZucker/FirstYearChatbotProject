from bs4 import BeautifulSoup

soup = BeautifulSoup(open("youtube.htm"))


with open("parseddata.txt", "wb") as file:
    for link in soup.find_all('img'):
        print  link.get('src')
        file.write(link.get('src')+"\n")

"""
Ce fichier permet de creer la base de donnees sur Game of Thrones via le site gameofthrones.fandom.com/wiki/ necessaire au chatbot.
"""

from os.path import dirname, realpath
import requests

from bs4 import BeautifulSoup
from textblob import TextBlob, classifiers
from owlready2 import *
from random import randint
import shelve

ontology_path = "file://" + dirname(realpath(__file__)) + "/ontology/" + \
"ontologyGoT.owl"
ontology = get_ontology(ontology_path).load()

def generating_url(ontology):
	L = []
	url = "https://gameofthrones.fandom.com/wiki/"
	for individuals in ontology.individuals():
		i = 0
		for c in individuals.name:
			if c == '_':
				i = i+1
		if i == 1:
			L.append(url+individuals.name)
	return L

def creation_text(url):
	cookies = dict(BCPermissionLevel='PERSONAL')
	html = requests.get(url, cookies=cookies, headers={'User-agent':'Mozilla/5.0'})
	soup = BeautifulSoup(html.content,"html.parser")
	soup.prettify("latin-1")
	soup.encode("ascii","replace")
	for script in soup(["script", "style"]):
		script.extract()
	text = soup.get_text()
	lines = (line.strip() for line in text.splitlines())
	chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
	text = '\n'.join(chunk for chunk in chunks if chunk)
	for c in text:
		if ord(c) > 127:
			text = text.replace(c, u'')
			pass
	return text

def cleaning_text(text):
	text_cleaned = ''
	Li = []
	for i in range(len(text)):
		#print(words)
		if i < len(text)-5 and text[i:i+5] == '[src]' and len(Li) == 0:
			#cpt = cpt+1
			Li.append(i)
			#print("HEY")
			pass
		elif i < len(text)-14 and text[i:i+14] == 'Contents[show]' and len(Li) == 1:
			Li.append(i)
			pass
		if len(Li) == 2:
			text_cleaned = text[Li[0]+6:Li[1]-1]
			return text_cleaned
	return text_cleaned

def cleaning_text2(text):
	text_cleaned = ''
	Li = []
	l = len(text)
	for i in range(len(text)):
		#print(words)
		if i < len(text)-14 and text[i:i+14] == 'Contents[show]':
			l = i+14
		elif i > l and text[i:i+6] == 'Season' and len(Li) == 0:
			#cpt = cpt+1
			Li.append(i)
			#print("HEY")
			pass
		elif i > l and text[i:i+6] == 'Season' and len(Li) == 1:
			Li.append(i)
			pass
		if len(Li) == 2:
			text_cleaned = text[Li[0]+6:Li[1]-1]
			return text_cleaned
	return text_cleaned

def cleaning_final(text):
	D = ['them','at', 'in', 'for', 'of', 'the', 'and', 'to', 'a', "'s", 'by', 'though', 'as', 'through', '.', 'is', 'her', 'his', 'into', 'an', 'that']
	blob = TextBlob(text)
	#print(blob.words)
	temp = ''
	for line in blob.sentences:
		for words in line.split():
			if words not in D:
				#print("HAHA")
				#temp.remove(words)
				temp += words + ' '
		temp += '\n'
	return temp

def creation_tabset(text):
	text = text.split('\n')
	L = []
	List = ['Arya', 'Sansa', 'Eddard', 'Ned', 'Jon', 'Danearys', 'Joeffrey', 'Cersei', 'Hound']
	passe = True
	#print(text)
	for tokens in text:
		"""for c in tokens:
			if c in punctuation:
				tokens = tokens.replace(c, '')"""
		for words in tokens.split():
			#print(words)
			if words not in List:
				passe = False
			else:
				passe = True
				break
		if tokens != '' and passe == True:
			L.append((tokens, 'pos'))
	#L.append(('', 'neg'))
	return L

def creation_tabset2(text):
	text = text.split('\n')
	L = []
	List = ['Arya', 'Sansa', 'Eddard', 'Ned', 'Jon', 'Danearys', 'Joeffrey', 'Cersei', 'Hound']
	passe = True
	for tokens in text:
		"""for c in tokens:
			if c in punctuation:
				tokens = tokens.replace(c, '')"""
		for words in tokens.split():
			if words not in List:
				passe = False
			else:
				passe = True
				break
		if tokens != '' and passe == True:
			r = randint(0,10)
			if r > 4:
				L.append((tokens, 'neg'))
				pass
			else:
				L.append((tokens, 'pos'))
	#L.append(('', 'neg'))
	return L

def generating_url2(ontology):
	L = []
	url = "https://awoiaf.westeros.org/index.php/"
	for individuals in ontology.individuals():
		i = 0
		for c in individuals.name:
			if c == '_':
				i = i+1
		if i == 1:
			L.append(url+individuals.name)
	return L

def cleaning_text3(text):
	text_cleaned = ''
	Li = []
	for i in range(len(text)):
		if i < len(text)-8 and text[i:i+8] == 'Season 8' and len(Li) == 0:
			Li.append(i)
			pass
		elif i < len(text)-8 and text[i:i+8] == 'Contents' and len(Li) == 1:
			Li.append(i)
			pass
		if len(Li) == 2:
			text_cleaned = text[Li[0]+9:Li[1]-1]
			return text_cleaned
	return text_cleaned

d = shelve.open('basededonnees')
classifier = d['class']
d.close()
query = input("your question :")
prob_dist = classifier.prob_classify(query)
print(round(prob_dist.prob("pos"), 2))

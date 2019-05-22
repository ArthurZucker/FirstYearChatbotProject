import requests
from bs4 import BeautifulSoup
from textblob import classifiers
from os.path import dirname, realpath
from owlready2 import *
from textblob import TextBlob
import shelve

# utf-8 encoding

ontology_path = "file://" + dirname(realpath(__file__)) + "/../ontology/" + \
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

#url = "https://gameofthrones.fandom.com/wiki/Jon_Snow"

def creation_text(url):
	cookies = dict(BCPermissionLevel='PERSONAL')
	html = requests.get(url, cookies=cookies, headers={'User-agent':'Mozilla/5.0'})
	soup = BeautifulSoup(html.content,"html.parser")
	soup.prettify("latin-1")
	soup.encode("ascii","replace")
	for script in soup(["script", "style"]):
	    script.extract()    # rip it out

	text = soup.get_text()
	lines = (line.strip() for line in text.splitlines())
	chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
	text = '\n'.join(chunk for chunk in chunks if chunk)
	for c in text:
		if ord(c) > 127:
			text = text.replace(c, u'')
			pass
	return text
#print("hey")
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
	D = ['at', 'in', 'for', 'of', 'the', 'and', 'to', 'a', "'s", 'by', 'though', 'as', 'through', '.']
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
	text = text.split('.')
	L = []
	for tokens in text:
		"""for c in tokens:
			if c in punctuation:
				tokens = tokens.replace(c, '')"""
		if tokens != '':
			L.append((tokens, 'pos'))
	#L.append(('', 'neg'))
	return L

def creation_tabset2(text):
	text = text.split('.')
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
		if tokens != '' and passe == True:
			L.append((tokens, 'neg'))
	#L.append(('', 'neg'))
	return L

L = generating_url(ontology)
"""
L_tab = []

for url in L:
	text = creation_text(url)
	text_cleaned2 = cleaning_text2(text)
	text_cleaned2 = cleaning_final(text_cleaned2)
	text_cleaned = cleaning_text(text)
	text_cleaned = cleaning_final(text_cleaned)
	L_tab = L_tab + creation_tabset(text_cleaned) + creation_tabset2(text_cleaned2)
#print(text_cleaned)
"""
d = shelve.open('basededonnee')
L_tab = d['L_tab']
d.close()

#print(L_tab)
classifier = classifiers.NaiveBayesClassifier(L_tab)
#blob2 = TextBlob('Jon is the son of Ned Stark ?', classifier=classifier)
prob_dist = classifier.prob_classify("Is Jon Snow the son of Bran ?")
print(round(prob_dist.prob("pos"), 2))

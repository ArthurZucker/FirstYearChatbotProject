import nltk 
import urllib.request
#nltk.download('stopwords')
from os.path import dirname, realpath
from nltk.corpus import stopwords
from bs4 import BeautifulSoup
import database as data
from owlready2 import *	
from textblob import TextBlob
from textblob import classifiers

ontology_path = "file://" + dirname(realpath(__file__)) + "/../ontology/" + \
"ontologyGoT.owl"
ontology = get_ontology(ontology_path).load()

L = data.generating_url(ontology)
text = data.creation_text(L[0])
print(text)

text = data.cleaning_text(text)
print(text)
#data.replace('at ', ' ')
def cleaning_final(text):
	D = ['at', 'in', 'for', 'of', 'the', 'and', 'to', 'a', "'s", 'by', 'though', 'as', 'through', '.', 'that', 'into', 'is', 'him', 'her', 'his', 'them', 'this', 'he', 'she']
	blob = TextBlob(text)
	print(blob.words)
	temp = ''

	for line in blob.sentences:
		for words in line.split():
			if words not in D:
				#print("HAHA")
				#temp.remove(words)
				temp += words + ' '
		temp += '\n'
	return temp

text = cleaning_final(text)
print(text)
L = data.creation_tabset(text)
print(L)
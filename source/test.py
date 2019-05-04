# On importe les librairies dont on aura besoin pour ce t
import nltk
from os.path import dirname, realpath
from owlready2 import *

onto_path.append(dirname(dirname(realpath(__file__))) + "/ontology/")
ontologyGoT_path = onto_path[0] + "ontologyGoT.owl"
GoT = get_ontology("file://" + ontologyGoT_path).load()

def reply(sentence):
	sentence = sentence.split(",")
	print(sentence)
	tab = []
	for s in sentence:
		tokens = nltk.word_tokenize(s)
		tagged = nltk.pos_tag(tokens)
		tab.append(tagged)
	#print(tab)
	#print(len(tab))
	if len(tab) != 3:
		print("ERROR: question format")
		return
	else:
		print(GoT.search(is_a = GoT.Place))
		print(GoT.search(subclass_of = GoT.TheNorth))

reply("Winterfell, is the capital of, Winterfell")
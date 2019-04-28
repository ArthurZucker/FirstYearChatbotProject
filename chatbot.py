#! /usr/bin/env python

# -*- coding: utf-8 -*-

"""
This is a chatbot Game of Thrones
"""
from os import getcwd, chdir

from owlready2 import *			# pour charger l ontologie

from source.window import * # pour charger l interface graphique
# from src.Younes import *
# from src.Romain import *

ontology_path = "file://" + os.path.dirname(os.path.abspath(__file__)) + \
"/ontology/" + "ontologyGoT.owl"
GoT = get_ontology(ontology_path).load()

def reply(mode, query, ontology):
	"""
	If the query is right according to the mode, this function looks for an
	answer in the ontology.
	:param mode: 0 ( = one line mode) or 1 ( = Multi line mode)
	:param query: the query to ask to the chatbot
	:param ontology: the ontology
	:type mode: int
	:type query: string
	!type ontology: owlready2.namespace.Ontology
	:return: the answer of the query
	:rtype: string
	"""
  # format requete : "Individual #1", "Property", "Individual #2"
	if mode == 0:
		query = query.split(",")
		if len(query) != 3:
			errorBox()
			return None
	else:
		for str in query:
			if str == "":
				errorBox()
				return None
	individual_1 = query[0]
	property = query[1]
	individual_2 = query[2]
  # ...
	answer = ""
	return answer

still = True
while still:
	mode = selectModeBox()
	if mode == None:
		endBox()
		continue
	query = queryBox(mode)
	if query == None:
		cancelBox()
	else:
		answer = reply(mode, query, GoT)
		if answer != None:
			answerBox(mode, query, answer)
	still = endBox()

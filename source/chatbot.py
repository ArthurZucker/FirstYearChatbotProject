#! /usr/bin/env python3

"""
Ce fichier execute le chatbot en faisant appel au fonctions des modules se situant dans le repertoire source.
"""

from os.path import dirname, realpath

from owlready2 import *	# pour charger l ontologie

from ui import * # pour charger l interface graphique

from processing import reply # pour charger la reponse

from comment import * # pour commenter l ontologie

ontology_path = "file://" + dirname(dirname(realpath(__file__))) + "/ontology/" + "ontologyGoT.owl"
ontology = get_ontology(ontology_path).load()

initComment(ontology)

answerList = ["The history :\n\n"]

still = True
while still:
	mode = None
	try:
		mode = selectModeBox()
	except AssertionError :
		imageBox()
	if mode == None:
		still = endBox()
		continue
	query = queryBox(mode)
	if query == None:
		cancelBox()
	else:
		answer, queryFound = reply(mode, query, ontology)
		if answer != None:
			result = answerBox(mode, query, queryFound, answer,answerList)
			answerList.append('\n'+result)
	still = endBox()

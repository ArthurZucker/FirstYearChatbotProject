#! /usr/bin/env python

# -*- coding: utf-8 -*-

"""
Ce fichier execute le chatbot en faisant appel au fonctions des modules se situant dans le repertoire source.
"""

from os.path import dirname, realpath
from threading import Thread

from owlready2 import *	# pour charger l ontologie

from source.ui import * # pour charger l interface graphique

from source.processing import reply # pour charger la reponse

ontology_path = "file://" + dirname(realpath(__file__)) + "/ontology/" + \
"ontologyGoT.owl"
ontology = get_ontology(ontology_path).load()

answerList = []
thread_answer = Thread()

still = True
while still:
	# ERROR : appuie sur la photo
	print(selectModeBox())
	mode = selectModeBox()
	print(mode)
	if mode == None:
		still = endBox()
		continue
	query = queryBox(mode)
	if query == None:
		cancelBox()
	else:
		answer, queryFound = reply(mode, query, ontology)
		if answer != None:
			result = answerBox(mode, query, queryFound, answer)
			answerList.append(result)
	thread_answer.start(historyBox,answerList)
	still = endBox()

#! /usr/bin/env python

# -*- coding: utf-8 -*-

"""
This is a chatbot Game of Thrones.
"""

from os.path import dirname, abspath

from owlready2 import *			# pour charger l ontologie

from source.window import * # pour charger l interface graphique
from source.reply import * 	# pour charger la reponse
 														# fichier de Younes et Romain

ontology_path = "file://" + dirname(abspath(__file__)) + "/ontology/" + \
"ontologyGoT.owl"
GoT = get_ontology(ontology_path).load()

still = True
while still:
	mode = selectModeBox()
	if mode == None:
		still = endBox()
		continue
	query = queryBox(mode)
	if query == None:
		cancelBox()
	else:
		answer = reply(mode, query, GoT)
		if answer != None:
			answerBox(mode, query, answer)
	still = endBox()

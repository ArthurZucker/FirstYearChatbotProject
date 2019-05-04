#! /usr/bin/env python

# -*- coding: utf-8 -*-

"""
Ce fichier execute le chatbot.
"""
# Jon_Snow,isLoyalTo,Sansa_Stark?
from os.path import dirname, realpath

from owlready2 import *	# pour charger l ontologie

from source.ui import * # pour charger l interface graphique

from source.processing import reply # pour charger la reponse

ontology_path = "file://" + dirname(realpath(__file__)) + "/ontology/" + \
"ontologyGoT.owl"
ontology = get_ontology(ontology_path).load()

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
		answer = reply(mode, query, ontology)
		if answer == None:
			noResultBox()
		elif answer == 1:
			still = endBox()
			continue
		else:
			answerBox(mode, query, answer)
	still = endBox()

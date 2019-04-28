#! /usr/bin/env python

# -*- coding: utf-8 -*-

from .window import endBox # pour charger l interface graphique

"""
This is the program that replies the user.
"""

def reply(mode, query, ontology):
	"""
	If the query is right according to the mode, this function looks for an
	answer in the ontology.
	:param mode: 0 ( = one line mode) or 1 ( = Multi line mode)
	:param query: the query to ask to the chatbot
	:param ontology: the ontology
	:type mode: int
	:type query: str
	!type ontology: owlready2.namespace.Ontology
	:return: the answer of the query
	:rtype: str
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

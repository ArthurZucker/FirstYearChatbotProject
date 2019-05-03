#! /usr/bin/env python

# -*- coding: utf-8 -*-

"""
Ce fichier contient les fonctions necessaires au chatbot pour repondre a la requete de l utilisateur grace au parcourt sur l ontologie.
"""

from .window import endBox # pour charger l interface graphique

"""
Ce programme cree la reponse que retourne le chatbot.
"""

def reply(mode, query, ontology):
	"""
	Recherche une reponse a la requete donnee dans l ontologie, si la requete est correcte eu egard au mode choisi.

	:param int mode: le mode selectionne soit 0 (mode une ligne) soit 1 (mode plusieurs lignes).
	:param query: la requete a demander au chatbot.
	:param owlready2.namespace.Ontology ontology: l ontologie.
	:type query: str ou list(str)
	:return: la reponse de la requete.
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

def elem_question(question, GoT):
	if (question.find(",") == 2 and question.find("?") == 1):
		question.replace("?","")
		x = question.split(",")
		if (x[0] in list(GoT.individuals()) and x[1] in list(GoT.properties()) and x[2] in list(GoT.individuals())):
			return x
		else:
			errorbox()
			return None
	else:
		errorbox()
		return None

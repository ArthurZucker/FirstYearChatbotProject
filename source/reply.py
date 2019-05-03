#! /usr/bin/env python

# -*- coding: utf-8 -*-

"""
Ce fichier contient les fonctions necessaires au chatbot pour repondre a la requete de l utilisateur grace au parcourt sur l ontologie.
"""

from .window import endBox # pour charger l interface graphique


def check(raw_query, ontology):
	"""
	Verifie si la requete est valide.

	:param str query: la requete.
	:param owlready2.namespace.Ontology ontology: l ontologie.
	"""
	if (raw_query.find(",") == 2 and raw_query.find("?") == 1):
		raw_query.replace("?","")
		query = raw_query.split(",")
		if (
		query[0] in list(ontology.individuals()) and
		query[1] in list(ontology.properties()) and
		query[2] in list(ontology.individuals())):
			return query
		else:
			return None
	else:
		return None

def reply(mode, raw_query, ontology):
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
		query = check(raw_query, ontology)
		if query == None:
			errorBox()
		# query = query.split(",")
		# if len(query) != 3:
		# 	errorBox()
		# 	return None
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

#! /usr/bin/env python

# -*- coding: utf-8 -*-

"""
Ce fichier contient les fonctions necessaires au chatbot pour repondre a la requete de l utilisateur grace au parcourt sur l ontologie.
"""

from .ui import endBox, notInOntologyBox # pour charger l interface graphique

def check(mode, raw_query, ontology):
	"""
	Verifie si la requete entree a le bon format eu egard au mode choisi. Puis, met la requete sous la forme conventionnelle.

	:param int mode: le mode selectionne soit 0 (mode une ligne) soit 1 (mode plusieurs lignes).
	:param raw_query: la requete.
	:param owlready2.namespace.Ontology ontology: l ontologie.
	:type raw_query: str ou list(str)
	:return: la requete sous forme de liste.
	:rtype: list(str) ou None
	"""
	if mode == 0:
		if (raw_query.find(",") == 2 and raw_query.find("?") == 1):
			raw_query.replace("?","")
			query = raw_query.split(",")
			if (
			query[0] in list(ontology.individuals()) and
			query[1] in list(ontology.properties()) and
			query[2] in list(ontology.individuals())):
				return query
	elif mode == 1:
		for str in raw_query:
			if str == "":
				return None
		return raw_query
	return None

def isInOntology(query, ontology):
	"""
	Retourne True si les elements de la requete sont dans l ontologie et False sinon.

	:param list(str) query: la requete.
	:param owlready2.namespace.Ontology ontology: l ontologie.
	:return: True si les elements de la requete sont dans l ontologie et False sinon.
	:rtype: bool
	"""
	isInOntology = (
	query[0] in list(ontology.individuals()) and
	query[1] in list(ontology.properties()) and
	query[2] in list(ontology.individuals()))
	return isInOntology

def answer(query, ontology):
	"""
	Recherche une reponse a la requete dans l ontologie.

	:param list(str) query: la requete.
	:param owlready2.namespace.Ontology ontology: l ontologie.
	:return: la reponse a la requete.
	:rtype: str
	"""
	# Creation d'une liste de réponses
	# Jon_Snow, isLoyalTo, Sansa_Stark ?
	lists = list(ontology.query[0].query[1]) # Exemple si query[0] = Jon Snow et query[1] = isLoyalto
	# lists = [GoT.Danearys, GoT.Arya, GoT.Sansa]
	if ontology.quey[2] in lists:
		return "Yes"
	return "No"
	

def reply(mode, raw_query, ontology):
	"""
	Si la requete donnee est correcte, retourne la reponse de la requete.

	:param int mode: le mode selectionne soit 0 (mode une ligne) soit 1 (mode plusieurs lignes).
	:param query: la requete a demander au chatbot.
	:param owlready2.namespace.Ontology ontology: l ontologie.
	:type query: str ou list(str)
	:return: la reponse de la requete.
	:rtype: str
	"""
	query = check(mode, raw_query, ontology)
	if query == None:
		errorBox()
	elif isInOntology(query, ontology):
		answer = answer(query,ontology)
		return answer
	else:
		notInOntologyBox()
	return None

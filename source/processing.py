#! /usr/bin/env python

# -*- coding: utf-8 -*-

"""
Ce fichier contient les fonctions necessaires au chatbot pour repondre a la requete de l utilisateur grace au parcourt sur l ontologie.
"""

from .ui import endBox, notInOntologyBox, formatErrorBox # pour charger l interface graphique

def check(mode, raw_query, ontology):
	"""
	Verifie si la requete entree a le bon format eu egard au mode choisi.
	Le format adequat pour le mode sur une ligne est :
	instance1,propriete,instance2?
	Puis, met la requete sous la forme conventionnelle.

	:param int mode: le mode selectionne soit 0 (mode une ligne) soit 1 (mode plusieurs lignes).
	:param raw_query: la requete.
	:param owlready2.namespace.Ontology ontology: l ontologie.
	:type raw_query: str ou list(str)
	:return: la requete sous forme de liste.
	:rtype: list(str) ou None
	"""
	if mode == 0:
		if (raw_query.find(',') == 2 and raw_query.find('?') == 1):
			raw_query.replace('?','')
			query = raw_query.split(",")
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
	:return: un 4-uplet compose de : True si les elements de la requete sont dans l ontologie et False sinon, les objets correspondant aux elements de la requete.
	:rtype: (bool, owlready2.entity.ThingClass, owlready2.prop.ObjectPropertyClass, owlready2.entity.ThingClass)
	"""
	isInOntology = False
	indiv1 = None
	prop = None
	indiv2 = None
	for entities in ontology.individuals():
		# Initialisation pour éviter les problèmes
		if query[0] == entities.name:
			isInOntology = True
			indiv1 = entities
			break
	if indiv1==None:
		print("indiv1 pas dans les entite")
		formatErrorBox()
	# EREUR ICI
	if isInOntology:
		isInOntology = False
		for entities in dir(indiv1):
			if query[1] == entities.name:
				isInOntology = True
				prop = entities
				break
		if prop==None:
			print("Propriete inexistante pas dans les entite")
			formatErrorBox()
		if isInOntology:
			isInOntology = False
			for entities in ontology.individuals():
				if query[2] == entities.name:
					isInOntology = True
					indiv2 = entities
					break
		if indiv2==None:
			print("indiv2 inexistante pas dans les entite")
			formatErrorBox()
	return (isInOntology, indiv1, prop, indiv2) #Retourne un tuple => utile pour la suite pour
												# éviter de tout reparcourir

def answer(query, ontology):
	"""
	Recherche une reponse a la requete dans l ontologie.

	:param list(str) query: la requete.
	:param owlready2.namespace.Ontology ontology: l ontologie.
	:return: la reponse a la requete.
	:rtype: str
	"""
	#Vérification de la condition:
	liste = isInOntology(query, ontology)
	print(liste)
	if liste[0]:
		if liste[3] in liste[1].liste[2]:
			return "Yes"
		return "No"
	formatErrorBox()
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
		formatErrorBox()
	elif isInOntology(query, ontology)[0]:
		response = answer(query,ontology)
		return response
	else:
		notInOntologyBox()
	return None

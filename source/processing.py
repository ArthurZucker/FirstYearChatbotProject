#! /usr/bin/env python

# -*- coding: utf-8 -*-

"""
Ce fichier contient les fonctions necessaires au chatbot pour repondre a la requete de l utilisateur grace au parcourt sur l ontologie.
"""

from .ui import endBox, notInOntologyBox, formatErrorBox, noResultBox # pour charger l interface graphique

def check2(sentence):
	"""D = {"loyal":"isLoyalTo"}
	raw_query = raw_query.split(",")

	s2 = raw_query[1].split(" ")

	for words in s2:
		if words in D:
			#print(words)
			raw_query[1] = raw_query[1].replace(words, D[words])
		else:
			raw_query[1] = raw_query[1].replace(words, "")

	return "".join(raw_query)
	#print(sentence[1])"""

	D = {"loyal":"isLoyalTo", "arya":"Arya_Stark", "sansa":"Sansa_Stark", "cersei":"Cersei_Lannister"}

	#sentence = "Arya , is loyal to, Sansa ?"

	sentence = sentence.split(",")

	s2 = sentence[1].split(" ")
	#print(s2)
	#print(sentence)
	for i in range(len(sentence)):
		sentence[i] = sentence[i].lower()
		s2 = sentence[i].split(" ")
		for words in s2:
			if words in D:
				print(D[words])
				sentence[i] = sentence[i].replace(words, D[words])
				print(sentence[i])
			else:
				sentence[i] = sentence[i].replace(words, "")
	return "".join(sentence)


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
	:return: la requete sous forme de liste de str.
	:rtype: list(str) ou None
	"""
	query = None
	if mode == 0:
		if (raw_query.find(',') != -1 and raw_query.find('?') != -1):
			tempQuery = raw_query.replace('?','')
			query = tempQuery.split(",")
	elif mode == 1:
		for str in raw_query:
			if str == "":
				return None
		query = raw_query
	return query

def isInOntology(query, ontology):
	"""
	Verifie la presence des entites recherchees dans l ontologie. Retourne un 4-uplet compose de : True si tous les elements de la requete sont dans l ontologie et False sinon, l instance du premier terme, le nom de la propriete, l instance du deuxieme terme.

	:param list(str) query: la requete.
	:param owlready2.namespace.Ontology ontology: l ontologie.
	:return: un 4-uplet compose de : True si tous les elements de la requete sont dans l ontologie et False sinon, l instance du premier terme, le nom de la propriete, l instance du deuxieme terme.
	:rtype: (bool, owlready2.entity.ThingClass ou None, str ou None, owlready2.entity.ThingClass ou None)
	"""
	isInOntology = False
	individual1 = None
	propertyName = None
	individual2 = None

	# verifier la fonction check 2
	# raw_query = check2(raw_query)

	for individual in ontology.individuals():
		if query[0] == individual.name:
			isInOntology = True
			individual1 = individual
			break
	if isInOntology:
		isInOntology = False
		for str1 in dir(individual1):
			if query[1] == str1:
				isInOntology = True
				propertyName = str1
				# search_one
				# searchList = ontology.search(iri = "*"+propertyName+"*")
				# if len(searchList) == 1 and propertyName == searchList[0].name:
				# 	property = searchList[0]
				# else:
				# 	print("Error : at least two properties are similar.")
				break
		if isInOntology:
			isInOntology = False
			for individual in individual1.__getattr__(propertyName):
				if query[2] == individual.name:
					isInOntology = True
					individual2 = individual
					break
	return (isInOntology, individual1, propertyName, individual2)

def answer(individual1, propertyName, individual2, ontology):
	"""
	Recherche une reponse a la requete dans l ontologie, donnee sous forme d instance pour les individus et sous la forme de str pour la propriete.

	:param owlready2.entity.ThingClass individual1: l instance 1
	:param str propertyName: le nom de la propriete.
	:param owlready2.entity.ThingClass individual2: l instance 2
	:param owlready2.namespace.Ontology ontology: l ontologie.
	:return: la reponse a la requete.
	:rtype: str
	"""
	if individual2 in individual1.__getattr__(propertyName):
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
		formatErrorBox()
		return None
	isInOnto, individual1, propertyName, individual2 = isInOntology(query, ontology)
	if isInOnto:
		response = answer(individual1, propertyName, individual2, ontology)
		if response == None:
			noResultBox()
		return response
	else:
		notInOntologyBox()
	return None

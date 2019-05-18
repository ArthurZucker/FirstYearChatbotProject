#! /usr/bin/env python

# -*- coding: utf-8 -*-

"""
Ce fichier contient les fonctions necessaires au chatbot pour repondre a la requete de l utilisateur grace au parcourt sur l ontologie.
"""

from .ui import endBox, notInOntologyBox, formatErrorBox, noResultBox # pour charger l interface graphique

# Superbe fonction crée par youyou
# Parcours l'ontologie et récupére l'individu qui a  plus de 60% de similitude avec le vrai nom

def FindIndivdualByName(name, ontology):
	name = name.strip()
	for individuals in ontology.individuals():
		iterate = 0
		str1 = individuals.name
		for c in range(min(len(name), len(str1))):
			if str1[c].lower() == (name)[c].lower():
				iterate = iterate+1
				
		percent = (iterate/min(len(name), len(str1)))*100
		#print(percent)
		if percent >= 60:
				propertyName = str1
				isInOntology = True
				return individuals
				break
	return None
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
	punctuation = {'?', ',', '.', ':', ';'}
	query = None
	if mode == 0:
		if (raw_query.find(',') != -1 and raw_query.find('?') != -1):
			tempQuery = raw_query.replace('?','')
			query = tempQuery.split(",")
			indice = 0
		else:
			for letters in raw_query:
				if letters in punctuation:
					raw_query = raw_query.replace(letters, '')
			query = raw_query
			indice = 1
	elif mode == 1:
		for str in raw_query:
			if str == "":
				return None
		query = raw_query
		indice = 2
	return query, indice

def isInOntology(query, ontology):
	"""
	Verifie la presence des entites recherchees dans l ontologie. Retourne un 4-uplet compose de : True si tous les elements de la requete sont dans l ontologie et False sinon, l instance du premier terme, le nom de la propriete, l instance du deuxieme terme.

	:param list(str) query: la requete.
	:param owlready2.namespace.Ontology ontology: l ontologie.
	:return: un 4-uplet compose de : True si tous les elements de la requete sont dans l ontologie et False sinon, l instance du premier terme, le nom de la propriete, l instance du deuxieme terme.
	:rtype: (bool, owlready2.entity.ThingClass ou None, str ou None, owlready2.entity.ThingClass ou None)
	"""
	#print(query)
	indice = query[1]
	query = query[0]
	isInOntology = False
	individual1 = None
	propertyName = None
	individual2 = None
	if indice == 0 or indice == 2:
		query[0] = query[0].replace("_", " ")
		individual1 = FindIndivdualByName(query[0], ontology)
		if individual1 != None:
			isInOntology = True
		if isInOntology :
			isInOntology = False
			for str1 in dir(individual1) :
				if query[1] == str1 :
					isInOntology = True
					propertyName = str1
					# pour recuperer l objet propriete :
					# searchList = ontology.search(iri = "*"+propertyName+"*")
					# if len(searchList) == 1 and propertyName == searchList[0].name:
					# 	property = searchList[0]
					# else:
					# 	print("Error : at least two properties are similar.")
					break
			if not isInOntology :
				if query[1].find(" ") == -1 :
					for str1 in dir(individual1) :
						if str1.find(query[1]) != -1 :
							isInOntology = True
							propertyName = str1
							break
				else :
					query[1] = query[1].replace(" ", "")
					#print(query[1])
					for str1 in dir(individual1):
						iterate = 0
						for c in range(min(len(query[1]), len(str1))):
							if str1[c].lower() == (query[1])[c].lower():
								iterate = iterate+1
						#print(iterate)
						percent = (iterate/min(len(query[1]), len(str1)))*100
						if percent > 85:
							#print("Youhou")
							propertyName = str1
							isInOntology = True
							break
			if isInOntology :
				#print(propertyName)
				"""isInOntology = False
				for individual in individual1.__getattr__(propertyName):
					if query[2] == individual.name :
						isInOntology = True
						individual2 = individual
						break
			if not isInOntology :
				query[2] = query[2].title()
				query[2] = query[2].strip()
				#print(query[2])
				if query[2].find(" ") == -1:
					search = ontology.search_one(iri = "*"+query[2]+"*")
				else: 
					individualWords = query[2].replace(" ","_")
					search = ontology.search_one(iri = "*"+individualWords+"*")	
				if search :
					individual2 = search
					isInOntology = True"""
				individual2 = FindIndivdualByName(query[2], ontology)
				if individual2 == None:
					isInOntology = False
		elif indice == 1:
			pass
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

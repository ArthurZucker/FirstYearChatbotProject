"""
Ce fichier contient les fonctions nécessaires au chatbot pour répondre à la requête de l'utilisateur grace au parcours sur l'ontologie ou à une base de données.
"""

from textblob import TextBlob, classifiers
import shelve

from ui import endBox, notInOntologyBox, formatErrorBox, noResultBox # pour charger l'interface graphique
from comment import getComment # pour afficher la probabilité

def FindIndivdualByName(name, ontology):
	"""
	Parcourt l'ontologie et récupere l'individu qui a plus de 60% de similitude avec le nom veritable.

	:param str name: le nom de l'individu recherché.
	:param owlready2.namespace.Ontology ontology: l'ontologie.
	:return: l'instance correspondant à l'individu ou None si non trouvé.
	:rtype: owlready2.entity.ThingClass ou None
	"""
	name = name.strip()
	for individuals in ontology.individuals():
		iterate = 0
		str1 = individuals.name
		str1Len = len(str1)
		nameLen = len(name)
		for c in range(min(nameLen, str1Len)):
			if str1[c].lower() == name[c].lower():
				iterate = iterate + 1

		percent = (iterate/min(nameLen, str1Len))*100
		if percent >= 60:
			return individuals
	return None

def check(mode, raw_query, ontology):
	"""
	Vérifie si la requête entrée à le bon format eu egard au mode choisi.
	Le format adéquat pour le mode sur une ligne est :
	instance1,propriété,instance2?
	Puis, met la requête sous la forme conventionnelle.

	:param int mode: le mode selectionné : soit 0 (mode une ligne), soit 1 (mode plusieurs lignes), soit 2 (mode libre).
	:param raw_query: la requête.
	:param owlready2.namespace.Ontology ontology: l'ontologie.
	:type raw_query: str ou list(str)
	:return: un couple formé de la requête sous forme de liste(str) et un booléen décrivant le mode de saisie.
	:rtype: (list(str) ou None, bool)
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
	elif mode == 2:
		query = raw_query
		indice = 1
	return query, indice

def isInOntology(query, indice, ontology):
	"""
	Vérifie la présence des entités recherchées dans l'ontologie.
	Si la requête demandée n'est pas exactement dans l'ontologie, la fonction va chercher et renvoyer ce qui correspond à plus 85% a la donnée initiale.
	Retourne un 4-uplet composé de : True si tous les éléments de la requête sont dans l'ontologie et False sinon, l'instance du premier terme, le nom de la propriété, l'instance du deuxieme terme.

	:param list(str) query: la requête.
	:param bool'indice: le booléen décrivant le mode de saisie.
	:param owlready2.namespace.Ontology ontology: l'ontologie.
	:return: un 4-uplet compose de : True si tous les éléments de la requête sont dans l'ontologie et False sinon, l'instance du premier terme, le nom de la propriété, l'instance du deuxieme terme. Si l'un des termes n'est pas trouvé, il est retourné None à la place.
	:rtype: (bool, owlready2.entity.ThingClass ou None, str ou None, owlready2.entity.ThingClass ou None)
	"""
	isInOntology = False
	individual1 = None
	propertyName = None
	individual2 = None
	if indice == 0 or indice == 2:
		individualName = query[0].replace("_", " ")
		individual1 = FindIndivdualByName(individualName, ontology)
		if individual1 != None:
			isInOntology = True
		if isInOntology :
			isInOntology = False
			for str1 in dir(individual1) :
				if query[1] == str1 :
					isInOntology = True
					propertyName = str1
					break
			if not isInOntology :
				if query[1].find(" ") == -1 :
					for str1 in dir(individual1) :
						if str1.find(query[1]) != -1 :
							isInOntology = True
							propertyName = str1
							break
				else :
					propertyTempName = query[1].replace(" ", "")
					propertyLen = len(propertyTempName)
					for str1 in dir(individual1):
						iterate = 0
						str1Len = len(str1)
						for c in range(min(propertyLen, str1Len)):
							if str1[c].lower() == propertyTempName[c].lower():
								iterate = iterate+1
						percent = (iterate/min(propertyLen, str1Len))*100
						if percent > 85:
							propertyName = str1
							isInOntology = True
							break
		if isInOntology :
			isInOntology = False
			individual2 = FindIndivdualByName(query[2], ontology)
			if individual2 != None:
				isInOntology = True
	elif indice == 1:
		d = shelve.open('source/basededonnees')
		classifier = d['class']
		d.close()
		blob = TextBlob(query, classifier=classifier)
		return blob
	return (isInOntology, individual1, propertyName, individual2)

def answer(individual1, propertyName, individual2, ontology):
	"""
	Rend une réponse binaire a la requête par rapport à l'ontologie, donnée sous forme d'instance pour les individus et sous la forme de str pour la propriété.

	:param owlready2.entity.ThingClass individual1: l'instance n°1
	:param str propertyName: le nom de la propriété.
	:param owlready2.entity.ThingClass individual2: l'instance n°2
	:param owlready2.namespace.Ontology ontology: l'ontologie.
	:return: la réponse à la requête.
	:rtype: str
	"""
	if individual2 in individual1.__getattr__(propertyName):
		message = "Yes"
	else:
		message = "No"
	message += " (with probability " + getComment(individual1, propertyName, individual2, ontology) + ')'
	return message

def reply(mode, raw_query, ontology):
	"""
	Si la requête donnée est correcte, retourne la réponse de la requête.

	:param int mode: le mode selectionné soit 0 (mode une ligne) soit 1 (mode plusieurs lignes).
	:param raw_query: la requête à demander au chatbot.
	:param owlready2.namespace.Ontology ontology: l'ontologie.
	:type raw_query: str ou list(str)
	:return: un couple formé de la réponse de la requête et la requête que le chatbot a effectué ou None s'il n'a rien fait.
	:rtype: (str, list(str) ou None)
	"""
	query,indice = check(mode, raw_query, ontology)
	if indice != 1:
		if query == None:
			formatErrorBox()
			return None, None
		isInOnto, individual1, propertyName, individual2 = isInOntology(query, indice, ontology)
		if isInOnto:
			response = answer(individual1, propertyName, individual2, ontology)
			if response != None:
				queryFound = [individual1.name,propertyName,individual2.name]
				return response, queryFound
			else:
				noResultBox()
		else:
			notInOntologyBox()
		return None, None
	else:
		bolb = isInOntology(query, indice, ontology)
		if bolb.classify() == "pos":
			return ("Yes", query.split())
		else:
			return ("No", query.split())

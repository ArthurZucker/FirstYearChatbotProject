"""
Ce fichier contient les fonctions necessaires au chatbot pour repondre a la requete de l utilisateur grace au parcours sur l ontologie.
"""

from ui import endBox, notInOntologyBox, formatErrorBox, noResultBox # pour charger l interface graphique

def FindIndivdualByName(name, ontology):
	"""
	Parcourt l ontologie et recupere l individu qui a plus de 60% de similitude avec le nom veritable.
	:param str name: nom de l individu recherche.
	:param owlready2.namespace.Ontology ontology: l ontologie.
	:return: l instance correspondant a l individu ou None si non trouve.
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
	Verifie si la requete entree a le bon format eu egard au mode choisi.
	Le format adequat pour le mode sur une ligne est :
	instance1,propriete,instance2?
	Puis, met la requete sous la forme conventionnelle.

	:param int mode: le mode selectionne soit 0 (mode une ligne) soit 1 (mode plusieurs lignes).
	:param raw_query: la requete.
	:param owlready2.namespace.Ontology ontology: l ontologie.
	:type raw_query: str ou list(str)
	:return: un couple forme de la requete sous forme de liste de str et un booleen decrivant le mode de saisie.
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
	return query, indice

def isInOntology(query, indice, ontology):
	"""
	Verifie la presence des entites recherchees dans l ontologie.
	Si la requete demandee n est pas exactement dans l ontologie, la fonction va chercher et renvoyer ce qui correspond a plus 85% a la donnee initiale.
	Retourne un 4-uplet compose de : True si tous les elements de la requete sont dans l ontologie et False sinon, l instance du premier terme, le nom de la propriete, l instance du deuxieme terme.

	:param list(str) query: la requete.
	:param bool indice: booleen decrivant le mode de saisie.
	:param owlready2.namespace.Ontology ontology: l ontologie.
	:return: un 4-uplet compose de : True si tous les elements de la requete sont dans l ontologie et False sinon, l instance du premier terme, le nom de la propriete, l instance du deuxieme terme. Si l un des termes n est pas trouve, il est retourne None a la place.
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
		pass
	return (isInOntology, individual1, propertyName, individual2)

def answer(individual1, propertyName, individual2, ontology):
	"""
	Rend une reponse binaire a la requete par rapport a l ontologie, donnee sous forme d instance pour les individus et sous la forme de str pour la propriete.

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
	:param raw_query: la requete a demander au chatbot.
	:param owlready2.namespace.Ontology ontology: l ontologie.
	:type raw_query: str ou list(str)
	:return: un couple forme de la reponse de la requete et la requete que le chatbot a effectue ou None s il n a rien fait.
	:rtype: (str, list(str) ou None)
	"""
	query,indice = check(mode, raw_query, ontology)
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

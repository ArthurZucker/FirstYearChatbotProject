"""
Ce fichier contient les fonctions permettant d'interagir avec les commentaires des propriétés de l'ontologie qui servent à caracteriser les probabilités des relations.
"""

from os.path import dirname, realpath

from owlready2 import *	# pour charger l'ontologie

onto_path.append(dirname(dirname(realpath(__file__))) + "/ontology/")
ontology_path = "file://" + dirname(dirname(realpath(__file__))) + "/ontology/" + "ontologyGoT.owl"
ontology = get_ontology(ontology_path).load()


def initComment(ontology):
	"""
	Cette fonction parcourt l'ensemble des individus, puis l'ensemble de leurs propriétés, puis l'ensemble des individus possibles. Une fois l'individu n°1, la propriété et l'individu n°2 recuperés, on ajoute un commentaire contenant la probabilité de la relations les reliant.

	:param owlready2.namespace.Ontology ontology: l'ontologie.
	"""
	propertiesNames = [p.name for p in list(ontology.object_properties())]
	for individual1 in list(ontology.individuals()):
		data = dir(individual1)
		individual1Properties = []
		for propertyName in data:
			if propertyName in propertiesNames:
				property = ontology.search_one(iri = "*"+propertyName+"*")
				individual1Properties.append(property)

		if len(individual1Properties) > 0:
			for property in individual1Properties:
				individual2 = individual1.__getattr__(property.name)
				if len(individual2) > 0:
					for individual in individual2:
						comment[individual1, property, individual] = "1"
	ontology.save(file = onto_path[0] + "ontologyGoT.owl")

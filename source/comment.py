#! /usr/bin/env python

# -*- coding: utf-8 -*-

from os.path import dirname, realpath

from owlready2 import *	# pour charger l ontologie

onto_path.append(dirname(dirname(realpath(__file__))) + "/ontology/")
ontology_path = "file://" + dirname(dirname(realpath(__file__))) + "/ontology/" + \
"ontologyGoT.owl"
ontology = get_ontology(ontology_path).load()


def initComment(ontology):
	"""
	Cette fonction parcours l ensemble des individus et l ensemble de leurs proprietes vers l ensemble des individus possibles. Une fois l individu d entree, la propriete et l individu de sortie recuperes, on ajoute un commentaire contenant la probabilite.
	:param owlready2.namespace.Ontology ontology: l ontologie.
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

if __name__ == "__main__" :
	initComment(ontology)

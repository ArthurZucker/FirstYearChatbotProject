#!/usr/bin/env python

# -*- coding: utf-8 -*-

from os.path import dirname, realpath

from owlready2 import *

#https://pythonhosted.org/Owlready2/

onto_path.append(dirname(dirname(realpath(__file__))) + "/ontology/")
ontologyGoT_path = onto_path[0] + "ontologyGoT.owl"
GoT = get_ontology("file://" + ontologyGoT_path).load()

# creation d une nouvelle ontologie
# new_ontology_IRI = "http://www.semanticweb.org/jerome/ontologies/2019/3/newOntologyGoT.owl"
# newOntologyGoT_path = onto_path[0] + "newOntologyGoT.owl"
# newGoT = get_ontology(new_ontology_IRI)

def main():
	print("\nListe des classes :\n",list(GoT.classes()))
	print("\nListe des instances :\n",list(GoT.individuals()))
	print("\nListe des propriétés objet :\n",list(GoT.object_properties()))
	print("\nListe des propriétés data :\n",list(GoT.data_properties()))
	print("\nListe des propriétés :\n",list(GoT.properties()))

	print("\nListe des sous-classes de Place :\n",\
	GoT.search(subclass_of = GoT.Place))
	print("\nListe des entites avec le mot desire :\n",\
	GoT.search(iri = "*City"))
	print("\nListe des instances de Place :\n",\
	GoT.search(type = GoT.Place))
	print("\nListe des entites avec la relation desiree :\n",\
	GoT.search(isLoyalTo = "*"))
	print("\nListe des entites de Place :\n",\
	GoT.search(is_a = GoT.Place))

	# liste des proprietes
	print(dir(GoT.Jon_Snow),'\n')
	print(GoT.TheWesterlands.__dict__,'\n')

	# ajout d une propriete
	print(GoT.Jon_Snow.isLoyalTo,'\n')
	GoT.Jon_Snow.isLoyalTo.append(GoT.Arya_Stark)
	print(GoT.Jon_Snow.isLoyalTo)
	print(GoT.Arya_Stark in GoT.Jon_Snow.isLoyalTo)

	# sauvegarde dans un nouveau fichier
	GoT.save(file = onto_path[0] + "newOntologyGoT.owl")

if __name__ == "__main__":
	main()

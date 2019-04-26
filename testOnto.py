from owlready2 import *
#/path/to/your/local/ontology/repository
path = "/home/jerome/Informatique/chatbot/Ontology/"
file = "testOntologyGoT.owl"
onto = get_ontology("file://" + path + file).load()

print("\nListe des classes :\n",list(onto.classes()))
print("\nListe des instances :\n",list(onto.individuals()))
print("\nListe des propriétés :\n",list(onto.object_properties()))

print("\nListe des sous-classes de Place :\n",\
onto.search(subclass_of = onto.Place))
print("\nListe des entites avec le mot desire :\n",\
onto.search(iri = "*City"))
print("\nListe des instances de Place :\n",\
onto.search(type = onto.Place))
print("\nListe des entites avec la relation desiree :\n",\
onto.search(isFromHouse = "*"))

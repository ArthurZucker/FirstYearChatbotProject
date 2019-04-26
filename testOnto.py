from owlready2 import *
#/path/to/your/local/ontology/repository
path = "/home/jerome/Informatique/chatbot/Ontology/"
file = "testOntologyGoT.owl"
onto = get_ontology("file://" + path + file).load()

print(House.__class__)

from owlready2 import *
#/path/to/your/local/ontology/repository
onto_path.append("~/Informatique/chatbot")
onto = get_ontology("http://www.semanticweb.org/jerome/ontologies/2019/3/untitled-ontology-6")
onto.load()

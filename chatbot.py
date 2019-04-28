from owlready2 import *			# pour charger l ontologie
from source.window import * # pour charger l interface graphique
# from src.Younes import *
# from src.Romain import *

path = "./ontology/"
file = "ontologyGoT.owl"
GoT = get_ontology("file://" + path + file).load()

def reply(mode, query):
	if mode == 1:
		query = query.split(",")
		if len(query) != 3:
			errorBox()
			return None
	else:
		for str in query:
			if str == "":
				errorBox()
				return None
  # format requete : "Individual #1", "Property", "Individual #2"
	individual_1 = query[0]
	property = query[1]
	individual_2 = query[2]
  # ...
	answer = ""
	return answer

still = 1
while still == 1:
	mode = selectModeBox()
	query = queryBox(mode)
	if query == None:
		cancelBox()
	else:
		answer = reply(mode, query)
		if answer != None:
			answerBox(mode, query, answer)
	still = endBox()

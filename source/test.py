from os.path import dirname, realpath

from owlready2 import *

ontology_path = "file://" + dirname(realpath(__file__)) + "/.."+"/ontology/" + \
"ontologyGoT.owl"
ontology = get_ontology(ontology_path).load()

def FindIndivdualByName(name, ontology):
	name = name.strip()
	for individuals in ontology.individuals():
		iterate = 0
		str1 = individuals.name
		for c in range(min(len(name), len(str1))):
			if str1[c].lower() == (name)[c].lower():
				iterate = iterate+1

		percent = (iterate/min(len(name), len(str1)))*100
		print(percent)
		if percent >= 60:
				propertyName = str1
				isInOntology = True
				return individuals
				break
	return None
print('Enter the name :')
x = input()
print(FindIndivdualByName(x, ontology))

# def FindIndivdualByName(name, ontology):
# 	name = name.strip()
# 	tab_indiv = []
# 	for individuals in ontology.individuals():
# 		iterate = 0
# 		str1 = individuals.name
# 		for c in range(min(len(name), len(str1))):
# 			if str1[c].lower() == (name)[c].lower():
# 				iterate = iterate+1
#
# 		percent = (iterate/min(len(name), len(str1)))*100
# 		#print(percent)
# 		if percent >= 40:
# 				propertyName = str1
# 				tab_indiv.append((individuals, percent))
# 				#return individuals
# 				break
# 	if len(tab_indiv) == 0:
# 		return None
# 	indiv = tab_indiv[0]
# 	for T in tab_indiv:
# 		if indiv[1] < T[1]:
# 			indiv = T
# 			pass
# 	return indiv[0]

# if not isInOntology :
# 	query[2] = query[2].title()
# 	query[2] = query[2].strip()
# 	#print(query[2])
# 	if query[2].find(" ") == -1:
# 		search = ontology.search_one(iri = "*"+query[2]+"*")
# 	else:
# 		individualWords = query[2].replace(" ","_")
# 		search = ontology.search_one(iri = "*"+individualWords+"*")
# 	if search :
# 		individual2 = search

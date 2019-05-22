nom_prop = [p.name for p in list(ontologyGoT.properties)]
for indiv in list(ontologyGoT.individuals)
	all_p = dir(indiv)
	prop_indiv = []
	for p in all_p:
		if p in nom_prop:
			prop_indiv.append(p)
	for prop in prop_indiv:
		indiv_arrive = indiv.__getattr__(prop)
		for i in indiv_arrive:
			comment[indiv, prop, indiv_arrive] = 1
			print(comment[indiv, prop, indiv_arrive])


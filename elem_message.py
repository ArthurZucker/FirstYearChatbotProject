def elem_question(question, GoT):
	if (question.find(",") == 2 and question.find("?") == 1):
		question.replace("?","")
		x = question.split(",")
		if (x[0] in list(GoT.individuals()) and x[1] in list(GoT.properties()) and x[2] in list(GoT.individuals())):
			return x
		else:
			errorbox()
			return NULL
	else:
		errorbox()
		return NULL

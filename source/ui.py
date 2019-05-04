#!/usr/bin/env python

# -*- coding: utf-8 -*-

"""
Ce fichier contient les fonctions necessaires a l interface graphique du chatbot.
Chaque boite de dialogue est realisee par une fonction.
Il y a deux modes de saisie : soit un mode sur une ligne, soit un mode sur plusieurs lignes.
"""

from easygui import indexbox, enterbox, multenterbox, ccbox, msgbox, textbox

# http://easygui.sourceforge.net/tutorial.html#enterbox
# http://hebergement.u-psud.fr/iut-orsay/Pedagogie/MPHY/Python/easygui.pdf

def selectModeBox():
	"""
	Affiche la fenetre permettant de selectionner soit le mode une ligne, soit le mode sur plusieurs lignes.

	:return: le mode selectionne : soit 0 (mode une ligne), soit 1 (mode plusieurs lignes), soit None si l utilisateur a ferme la fenetre.
	:rtype: int ou None
	"""
	message = "Select the mode".center(80)
	title = "Chatbot Game of Thrones"
	choices = ("One line mode", "Multi line mode")
	mode = indexbox(message, title, choices)
	return mode

def queryBox(mode):
	"""
	Affiche la fenetre permettant d entrer la requete avec le mode de saisie dependant du mode donne en argument.

	:param int mode: mode est le mode selectionne par l utilisateur.
	:return: retourne la requete entree par l utilisateur.
	:rtype: str ou list(str)
	"""
	message = "Enter your query"
	title = "Chatbot Game of Thrones"
	if mode == 0:
		query = enterbox(message, title, default = "")
	elif mode == 1:
		fields = ("Individual #1", "Property", "Individual #2")
		query = multenterbox(message, title, fields)
	return query

def cancelBox():
	"""
	Affiche la fenetre indiquant que l utilisateur a appuye sur le bouton d annulation.
	"""
	title = "Chatbot Game of Thrones"
	message = ("Your query was void because you have clicked on the "
	"cancel button.").center(80)
	msgbox(message, title, "OK")

def errorBox():
	"""
	Affiche la fenetre indiquant que l utilisateur a entre une requete dont le format est incorrecte.
	"""
	title = "Chatbot Game of Thrones"
	message = ("Your query was void because the format used is wrong.\n"
	"Use format: <Individual>,<Property>,<Individual>?\n"
	"Please read README.md or README.txt.").center(80)
	msgbox(message, title, "OK")

def answerBox(mode, query, answer):
	"""
	Affiche la fenetre rappelant la requete entree par l utilisateur ainsi que la reponse donnee par le chatbot.

	:param int mode: mode est le mode selectionne par l utilisateur.
	:param query: la requete entree par l utilisateur.
	:param str answer: la reponse retournee par le chatbot.
	:type query: str ou list(str)
	"""
	title = "Chatbot Game of Thrones"
	if mode == 0:
		message = ("Your query was \"" + query + "\".\n"
		"The result of your query is:")
	elif mode == 1:
		message = ("Your query was \"" + ",".join(query) + "\".\n"
		"The result of your query is:")
	textbox(message, title, answer)

def endBox():
	"""
	Affiche la fenetre permettant de recommencer le jeu ou de le quitter.

	:return: True si l utilisateur clique sur "Continue" et False si l utilisateur clique sur "Quit" ou ferme la fenetre.
	:rtype: bool
	"""
	message = "Do you want to continue?".center(80)
	title = "Chatbot Game of Thrones"
	choices = ("Continue", "Quit")
	still = ccbox(message, title, choices)
	return still

def notInOntologyBox():
	"""
	Affiche la fenetre indiquant que l utilisateur a entre une requete dont les elements ne sont pas dans l ontologie.
	"""
	title = "Chatbot Game of Thrones"
	message = ("At least one of the terms of your query is not in the ontology").center(80)
	msgbox(message, title, "OK")

def noResultBox():
	"""
	Affiche la fenetre indiquant qu il n y a pas de resultat a la requete entree.
	"""
	title = "Chatbot Game of Thrones"
	message = ("There is no answer for your query in the ontology").center(80)
	msgbox(message, title, "OK")

def main():
	"""
	Fonction principale permettant de tester l interface graphique independamment du programme principale.
	"""
	still = True
	while still:
		mode = selectModeBox()
		if mode == None:
			still = endBox()
			continue
		query = queryBox(mode)
		if query == None:
			cancelBox()
		else:
			answer = "Yes or No or any answer"
			answerBox(mode, query, answer)
		still = endBox()

if __name__ == "__main__":
	main()

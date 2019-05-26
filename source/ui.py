#!/usr/bin/env python3

"""
Ce fichier contient les fonctions nécessaires à l'interface graphique du chatbot.
Chaque boite de dialogue est realisée par une fonction.
Il y à trois modes de saisie : soit un mode sur une ligne, soit un mode sur plusieurs lignes, soit un mode libre.
"""
from os.path import dirname, realpath

from easygui import indexbox, enterbox, multenterbox, ccbox, msgbox, textbox

image_path = dirname(realpath(__file__)) + "/image.gif"

def selectModeBox():
	"""
	Affiche la fenêtre permettant de selectionner soit le mode une ligne, soit le mode sur plusieurs lignes, soit le mode libre.

	:return: le mode selectionné : soit 0 (mode une ligne), soit 1 (mode plusieurs lignes), soit 2 (mode libre), soit None si l'utilisateur a fermé la fenêtre.
	:rtype: int ou None
	"""
	message = "Select the mode".center(80)
	title = "Chatbot Game of Thrones"
	choices = ("One line mode", "Multi line mode", "Free mode")
	mode = indexbox(message, title, choices, image = image_path)
	return mode

def queryBox(mode):
	"""
	Affiche la fenêtre permettant d'entrer la requête avec le mode de saisie selon le mode donné en argument.

	:param int mode: le mode selectionné par l'utilisateur.
	:return: retourne la requête entree par l'utilisateur.
	:rtype: str ou list(str)
	"""
	message = "Enter your query"
	title = "Chatbot Game of Thrones"
	if mode == 0:
		query = enterbox(message, title, default = "")
	elif mode == 1:
		fields = ("Individual #1", "Property", "Individual #2")
		query = multenterbox(message, title, fields)
	elif mode == 2:
		query = enterbox("Enter your free question (without '?'):", title, default = "")
	return query

def cancelBox():
	"""
	Affiche la fenêtre indiquant que l'utilisateur a appuyé sur le bouton d'annulation.
	"""
	title = "Chatbot Game of Thrones"
	message = ("Your query was void because you have clicked on the "
	"cancel button.").center(80)
	msgbox(message, title, "OK")

def formatErrorBox():
	"""
	Affiche la fenêtre indiquant que l'utilisateur a entré une requête dont le format est incorrecte.
	"""
	title = "Chatbot Game of Thrones"
	message = (
	"Your query was void because the format used is wrong.".center(80) + '\n' +
	"Use format: <Individual>,<Property>,<Individual>?".center(80) + '\n' +
	"Please read README.md or README.txt.".center(80))
	msgbox(message, title, "OK")

def answerBox(mode, query, queryFound, answer, answerList):
	"""
	Affiche la fenêtre rappelant la requête entrée par l'utilisateur, la réponse donnée par le chatbot ainsi que l'historique des questions/reponses.

	:param int mode: le mode selectionné par l'utilisateur.
	:param query: la requête entrée par l'utilisateur.
	:param list(str) queryFound: la requête effectuée par le chatbot composée du nom de l'individu 1, du nom de la propriété, du nom de l'individu 2.
	:param str answer: la réponse retournée par le chatbot.
	:param list(str) answerList: l'historique des questions/réponses.
	:type query: str ou list(str)
	:return: le message affiché.
	:rtype: str
	"""
	title = "Chatbot Game of Thrones"
	if mode == 0 or mode == 2:
		message = "Your query was \"" + query + "\"."
	elif mode == 1:
		message = "Your query was \"" + ",".join(query) + "?\"."
	message = message.center(65) + '\n'
	message += "The chatbot understood the query:".center(65) +'\n'
	message += ("\"" + " ".join(queryFound) + "?\"").center(65) + '\n'
	message += "The result of your query is:".center(65) + '\n\n'
	message +=	answer.center(65)
	textbox(message, title, answerList)
	return message

def endBox():
	"""
	Affiche la fenêtre permettant de recommencer le jeu ou de le quitter.

	:return: True si l'utilisateur clique sur "Continue" et False si l'utilisateur clique sur "Quit" ou ferme la fenêtre.
	:rtype: bool
	"""
	message = "Do you want to continue?".center(80)
	title = "Chatbot Game of Thrones"
	choices = ("Continue", "Quit")
	still = ccbox(message, title, choices)
	return still

def notInOntologyBox():
	"""
	Affiche la fenêtre indiquant que l'utilisateur a entré une requête dont les éléments ne sont pas dans l'ontologie.
	"""
	title = "Chatbot Game of Thrones"
	message = ("At least one of the terms of your query is not in the ontology").center(80)
	msgbox(message, title, "OK")

def noResultBox():
	"""
	Affiche la fenêtre indiquant qu il n'y à pas de résultat à la requête entrée.
	"""
	title = "Chatbot Game of Thrones"
	message = ("There is no answer for your query in the ontology").center(80)
	msgbox(message, title, "OK")

def imageBox():
	"""
	Affiche la fenêtre indiquant qu'il ne faut pas cliquer sur l'image.
	"""
	title = "Chatbot Game of Thrones"
	message = ("Do not click on the picture please.").center(80)
	msgbox(message, title, "OK")

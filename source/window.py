#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    This is the GUI of the chatbot
"""

from easygui import ynbox, enterbox, multenterbox, ccbox, msgbox, textbox

# http://easygui.sourceforge.net/tutorial.html#enterbox
# http://hebergement.u-psud.fr/iut-orsay/Pedagogie/MPHY/Python/easygui.pdf

def selectModeBox():
	"""
	Display a window in order to select between One line mode and Multi line
	mode.
	"""
	message = "Select the mode".center(80)
	title = "Chatbot Game of Thrones"
	choices = ("One line mode", "Multi line mode")
	mode = ynbox(message, title, choices)
	return mode

def queryBox(mode):
	message = "Enter your query"
	title = "Chatbot Game of Thrones"
	if mode == 1:
		query = enterbox(message, title, default = "")
	else:
		fields = ("Individual #1", "Property", "Individual #2")
		query = multenterbox(message, title, fields)
	return query

def cancelBox():
	title = "Chatbot Game of Thrones"
	message = ("Your query was void because you have clicked on the "
	"cancel button.").center(80)
	msgbox(message, title, "I apologize")

def errorBox():
	title = "Chatbot Game of Thrones"
	message = ("Your query was void because the format used is wrong. "
	"Please read README.md.").center(80)
	msgbox(message, title, "I apologize")

def answerBox(mode, query, answer):
	title = "Chatbot Game of Thrones"
	if mode == 1:
		message = ("Your query was \"" + query + "\".\n"
		"The result of your query is:")
	else:
		message = ("Your query was \"" + ",".join(query) + "\".\n"
		"The result of your query is:")
	textbox(message, title, answer)

def endBox():
	message = "Shall we continue?".center(80)
	title = "Chatbot Game of Thrones"
	choices = ("Continue", "Quit")
	still = ccbox(message, title, choices)
	return still

def main():
	still = 1
	while still == 1:
		mode = selectModeBox()
		query = queryBox(mode)
		if query == None:
			cancelBox()
		else:
			answer = "Yes or No or any answer"
			answerBox(mode, query, answer)
		still = endBox()

if __name__ == "__main__":
	main()

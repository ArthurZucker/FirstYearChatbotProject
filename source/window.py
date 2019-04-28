#!/usr/bin/env python

# -*- coding: utf-8 -*-

"""
This is the GUI of the chatbot.
Each box is made by a function. There are two input modes: a one line mode and a multi lines mode.
"""

from easygui import indexbox, enterbox, multenterbox, ccbox, msgbox, textbox

# http://easygui.sourceforge.net/tutorial.html#enterbox
# http://hebergement.u-psud.fr/iut-orsay/Pedagogie/MPHY/Python/easygui.pdf

def selectModeBox():
	"""
	Display a window in order to select between One line mode and Multi line
	mode.

	:return: 0 ( = one line mode) or 1 ( = Multi line mode).
	:rtype: int or None
	"""
	message = "Select the mode".center(80)
	title = "Chatbot Game of Thrones"
	choices = ("One line mode", "Multi line mode")
	mode = indexbox(message, title, choices)
	return mode

def queryBox(mode):
	message = "Enter your query"
	title = "Chatbot Game of Thrones"
	if mode == 0:
		query = enterbox(message, title, default = "")
	elif mode == 1:
		fields = ("Individual #1", "Property", "Individual #2")
		query = multenterbox(message, title, fields)
	return query

def cancelBox():
	title = "Chatbot Game of Thrones"
	message = ("Your query was void because you have clicked on the "
	"cancel button.").center(80)
	msgbox(message, title, "OK")

def errorBox():
	title = "Chatbot Game of Thrones"
	message = ("Your query was void because the format used is wrong. "
	"Please read README.md.").center(80)
	msgbox(message, title, "OK")

def answerBox(mode, query, answer):
	title = "Chatbot Game of Thrones"
	if mode == 0:
		message = ("Your query was \"" + query + "\".\n"
		"The result of your query is:")
	elif mode == 1:
		message = ("Your query was \"" + ",".join(query) + "\".\n"
		"The result of your query is:")
	textbox(message, title, answer)

def endBox():
	message = "Do you want to continue?".center(80)
	title = "Chatbot Game of Thrones"
	choices = ("Continue", "Quit")
	still = ccbox(message, title, choices)
	return still

def main():
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

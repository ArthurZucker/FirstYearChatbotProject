from easygui import *

#http://easygui.sourceforge.net/tutorial.html#enterbox
#http://hebergement.u-psud.fr/iut-orsay/Pedagogie/MPHY/Python/easygui.pdf

title = "Chatbot"
query = enterbox(msg = "Enter your query", title = title, default = "")
message = "Your query was \""+ query + "\".\nThe result of your query is :"
text = "Hello"
textbox(msg = message, title = title, text = text)

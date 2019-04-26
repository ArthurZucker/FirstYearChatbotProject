from easygui import *

#http://easygui.sourceforge.net/tutorial.html#enterbox
#http://hebergement.u-psud.fr/iut-orsay/Pedagogie/MPHY/Python/easygui.pdf

title = "Chatbot Game of Thrones"
still = 1

while still == 1:
  message = "Select the mode"
  message = message.center(80)
  choices = ("Simple mode", "Hard Mode")
  mode = ynbox(message, title, choices)
  if mode == 1:
    message = "Enter your query"
    query = enterbox(message, title, default = "")
    if query:
      message = "Your query was \"" + query + "\"." +\
      "\nThe result of your query is:"
      text = "Yes or No"
      textbox(message, title, text)

  message = "Shall we continue?"
  message = message.center(80)
  choices = ("Continue", "Quit")
  still = ccbox(message, title, choices)

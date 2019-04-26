from easygui import *

#http://easygui.sourceforge.net/tutorial.html#enterbox
#http://hebergement.u-psud.fr/iut-orsay/Pedagogie/MPHY/Python/easygui.pdf

title = "Chatbot Game of Thrones"
still = 1

while still == 1:
  cancel = False
  message = "Select the mode".center(80)
  choices = ("One line mode", "Multi line mode")
  mode = ynbox(message, title, choices)

  message = "Enter your query"
  if mode == 1:
    query = enterbox(message, title, default = "")
    if query is None:
      cancel = True
    else:
      message = "Your query was \"" + query + "\"." +\
      "\nThe result of your query is:"
  else:
    fields = ("Property #1", "Individual #1", "Property #2", "Individual #2")
    query = multenterbox(message, title, fields)
    if query is None:
      cancel = True
    else:
      message = "Your query was \"" + "".join(query) + "\"." +\
      "\nThe result of your query is:"

  if cancel:
    message = "Your query was void because you have clicked on the cancel \
button.".center(80)
    msgbox(message, title, "I apologize")
  else:
    text = "Yes or No"
    textbox(message, title, text)

  message = "Shall we continue?".center(80)
  choices = ("Continue", "Quit")
  still = ccbox(message, title, choices)

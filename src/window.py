from easygui import ynbox, enterbox, multenterbox, ccbox, msgbox, textbox

# http://easygui.sourceforge.net/tutorial.html#enterbox
# http://hebergement.u-psud.fr/iut-orsay/Pedagogie/MPHY/Python/easygui.pdf

def selectModeBox():
  message = "Select the mode".center(80)
  title = "Chatbot Game of Thrones"
  choices = ("One line mode", "Multi line mode")
  mode = ynbox(message, title, choices)
  return mode

def queryBox(mode):
  message = "Enter your query"
  title = "Chatbot Game of Thrones"
  cancel = False
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
  return (cancel, query, message)

def answerBox(cancel, query, message, answer):
  title = "Chatbot Game of Thrones"
  if cancel:
    message = "Your query was void because you have clicked on the \
cancel button.".center(80)
    msgbox(message, title, "I apologize")
  else:
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
    cancel, query, message = queryBox(mode)
    answer = "Yes or No"
    answerBox(cancel, query, message, answer)
    still = endBox()

if __name__ == "__main__":
  main()

from easygui import *

#http://hebergement.u-psud.fr/iut-orsay/Pedagogie/MPHY/Python/easygui.pdf

# msgbox("Ce moi de novembre est particulièrement pluvieux pour le sud de la France",\
#  title="Chatbot", ok_button= "Tout à fait",\
#  image="/nfs/home/sasl/eleves/main/3670819/Informatique/Python/TP1/giphy.gif")
#
# buttonbox(msg="Python est intéressant ?", title="Chatbot",\
# 	choices=("Tout à fait d'accord", "D'accord","Pas d'accord","Pas du tout d'accord"),\
# 	image = None)
# valeurs = multenterbox(msg="Veuillez saisir l'adresse", title="Chatbot",\
# 	fields=("Query"),\
# 	values=())# requete
# print(valeurs)

enterbox(msg = "Enter your query", title = "Chatbot", default = "")
text = "Hello"
textbox(msg = "Result of your query", title = "Chatbot", text = text)

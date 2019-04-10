from easygui import *

msgbox("Ce moi de novembre est particulièrement pluvieux pour le sud de la France",\
 title="Avis météo", ok_button= "Tout à fait",\
 image="/nfs/home/sasl/eleves/main/3670819/Informatique/Python/TP1/giphy.gif")

buttonbox(msg="Python est intéressant ?", title="Question",\
	choices=("Tout à fait d'accord", "D'accord","Pas d'accord","Pas du tout d'accord"),\
	image = None)
valeurs = multenterbox(msg="Veuillez saisir l'adresse", title="Coordonnées",\
	fields=("Nom","Prénom","Rue"," ","Code postal","Ville","Téléphone"),\
	values=())#nom, prenom,rue1,rue2,code,ville,tel
print(valeurs)
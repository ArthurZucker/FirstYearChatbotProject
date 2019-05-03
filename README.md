# Chatbot *Game of Thrones*

Ce git regroupe l'ensemble des fichiers nécessaires au lancement du chatbot.
Pour exécuter ce programme, il faut ouvrir un terminal, cloner le repertoire grâce à la commande :
>`git clone <lien_du_git>`

et exécuter le fichier principal grâce à la commande :
>`./chatbot.py` ou, si une erreur est renvoyée, `python3 chatbot.py`

##Version de python nécessaire :

Ce programme a été testé avec Python 3.7.3, il necessite Python 3 pour fonctionner.

## Packets nécessaires
Pour utiliser ce programme, il est nécessaire de posséder les packets suivants :
> `sys` `os` `types` `tempfile` `subprocess` `weakref` `re` `urllib` `warnings` `itertools` `owlready2` `easygui`

Vous pouvez les installer grâce à la commande suivante :
> `pip install <nom_du_packet>` ou `pip3 install <nom_du_packet>`

## Documentation

La documentation du programme est accessible en ouvrant le fichier `doc.html`.

## Ontologie

L'ontologie a été créée avec [*protégé*](https://protege.stanford.edu/). Le fichier `ontologyGoT.png` est un graphe des classes de l'ontologie. Le fichier `ontologyGoT.pdf` est un graphe complet de l'ontologie.

## Interface graphique

Toute l'interface graphique est regroupée dans le fichier `window.py`. Elle a
été réalisée grâce au module `easygui`.

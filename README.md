# Chatbot *Game of Thrones*

Ce git regroupe l'ensemble des fichiers nécessaires au lancement du chatbot.
Pour exécuter ce programme, il faut ouvrir un terminal, cloner le repertoire grâce à la commande :
>`git clone <lien_du_git>`

et exécuter le fichier principal grâce à la commande :
>`./chatbot.py`

## Packets nécessaires
Pour utiliser ce programme, il est nécessaire de posséder les packets suivants :
> `owlready2` `easygui`

Vous pouvez les installer grâce à la commande suivante :
> `pip install <packet>`

## Documentation

La documentation du programme est accessible en ouvrant le fichier `doc.html`.

## Ontologie

L'ontologie a été créée avec [*protégé*](https://protege.stanford.edu/). L'index de l'ontologie est accessible en ouvrant le fichier `indexOntology.html`. Le fichier `ontologyGoT.png` est un graphe des classes de l'ontologie. Le fichier `ontologyGoT.pdf` est un graphe complet de l'ontologie.

## Interface graphique

Toute l'interface graphique est regroupée dans le fichier `window.py`. Elle a
été réalisée grâce au module `easygui`.
___
Ce programme a été testé avec Linux Manjaro et Python 3.7.3.

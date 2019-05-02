Chatbot Game of Thrones

Ce dossier regroupe l'ensemble des fichiers nécessaires au lancement du chatbot.
Pour exécuter ce programme, il faut décomprésser le repertoire chatbot et exécuter le fichier principal grâce à la commande :
./chatbot.py
ou python3 chatbot.py si l'erreur suivante vous est renvoyée : "
Traceback (most recent call last):
  File "./chatbot.py", line 11, in <module>
    from owlready2 import *			# pour charger l ontologie
  File "/Library/Python/2.7/site-packages/owlready2/__init__.py", line 24, in <module>
    from owlready2.base            import *
  File "/Library/Python/2.7/site-packages/owlready2/base.py", line 20, in <module>
    import sys, os, types, tempfile, subprocess, weakref, re, urllib.request, warnings, itertools
ImportError: No module named request"

Version de python nécessaire:
Python3 doit être installé.

Packets nécessaires :

Pour utiliser ce programme, il est nécessaire de posséder les packets suivants :
owlready2
easygui

Vous pouvez les installer grâce à la commande suivante :
pip3 install <packet>
ou pip install <packet>
Documentation :

La documentation du programme est accessible en ouvrant le fichier doc.html.

Ontologie :

L'ontologie a été créée avec protégé (https://protege.stanford.edu/). Le fichier ontology_graphe.png est un graphe des classes de l'ontologie. Le fichier ontologyGoT.pdf est un graphe complet de l'ontologie.

Interface graphique :

Toute l'interface graphique est regroupée dans le fichier window.py. Elle a
été réalisée grâce au module easygui.
___
Ce programme a été testé avec Linux Manjaro et Python 3.7.3.

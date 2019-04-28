# Chatbot *Game of Thrones*
Ce git regroupe l'ensemble des fichiers nécessaires au lancement du chatbot.
Pour exécuter ce programme, il suffit de cloner le repertoire en faisant :
``git clone <lien_du_git>``
et de tapper la commande :
``./chatbot.py``
Le fichier ``doc.html`` est un lien symbolique vers la documentation du programme présente dans le dossier ``doc``. Le fichier ``indexOntology.html`` est un lien symbolique vers l'index de l'ontologie présent dans le dossier ```ontology``.
L'ontologie a été créée avec [*protégé*](https://protege.stanford.edu/) et se
situe dans le dossier ``ontology``. Le fichier ``ontology_graphe`` est un graphe de l'ontologie au format ``png``.
___
# Le reste est a changer (ne pas supprimer)

## Contenu du dossier ``source``

### Interface graphique
Toute l'interface graphique est regroupée dans le fichier ``window.py``. Elle a
été réalisée grâce au module ``easygui``. Chaque boite de dialogue est produite
par une unique fonction. Il y a un mode de saisie en une seule ligne et un mode
de saisie sur plusieurs lignes.
___
### Récupération du texte d'une page Internet
Tout est regroupé dans le fichier beautifulsoup.py
___
### Ontologie

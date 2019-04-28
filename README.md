# Chatbot *Game of Thrones*
Ce git regroupe l'ensemble des fichiers nécessaires au lancement du chatbot.
Le fichier à exécuter est le fichier ``chatbot.py``. Le fichier
``indexOntology`` est un lien symbolique vers l'index de l'ontologie présent
dans le dossier `ontology`.

## Contenu du dossier ``src``

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
L'ontologie a été créée avec [*protégé*](https://protege.stanford.edu/) et se
situe dans le dossier ``ontology``.
L'index de l'ontologie se situe dans ce dossier et permet de parcourir
l'ontologie via des fichiers ``html``. De plus, le fichier ``ontology_graphe``
est un graphe de l'ontologie au format ``png``.

# Chatbot *Game of Thrones*

Ce git regroupe l'ensemble des fichiers nécessaires au lancement du chatbot.

Pour exécuter ce programme, il faut ouvrir un terminal, cloner le repertoire grâce à la commande :
```sh
git clone <lien_du_git>
```

et exécuter le fichier principal grâce à la commande :
```sh
./chatbot.py
```
ou, si une erreur est renvoyée,
```
python3 chatbot.py
```

## Syntaxe

Pour utiliser le chatbot, il faut suivre la syntaxe suivante :
>`instance1`,`propriete`,`instance2`?

## Version de python nécessaire :

Ce programme a été testé avec Python 3.7.3, il necessite Python 3 pour fonctionner.

## Packets nécessaires

Pour utiliser ce programme, il est nécessaire de posséder les packets suivants :
> `sys` `os` `types` `tempfile` `subprocess` `weakref` `re` `urllib` `warnings` `itertools` `owlready2` `easygui`

Vous pouvez les installer grâce à la commande suivante :
```sh
pip install <nom_du_packet>
```
ou
```sh
pip3 install <nom_du_packet>
```

## Documentation

La documentation du programme est accessible en ouvrant le fichier `doc.html`.

## Ontologie

L'ontologie a été créée avec [*protégé*](https://protege.stanford.edu/). Le fichier `ontologyGoT.png` est un graphe des classes de l'ontologie. Le fichier `ontologyGoT.pdf` est un graphe complet de l'ontologie.

### Liste des instances présentes dans l'ontologie :
>Arryn, Arya_Stark, Baratheon, Benjen_Stark, BeyondTheWall, Bolton, Brandon_Stark, Cersei_Lannister, Daenerys_Targaryen, Dorne, DrownedGod, Eddard_Stark, FaithOfTheSeven, Frey, GreatStallion, Greyjoy, Jaqen_h_ghar, Jon_Snow, Lannister, LordOfLight, Lyanna_Stark, ManyFacedGod, Martell, Oberyn_Martell, OldGods, Rhaegar_Targaryen, Rickard_Stark, Rickon_Stark, Robb_Stark, Sansa_Stark, Stark, Targaryen, TheCrownlands, TheIronIslands, TheNorth, Theon_Greyjoy, TheReach, TheRiverlands, TheStormlands, TheVale, TheWesterlands, Tully, Tyrell, Tyrion_Lannister, Tywin_Lannister

## Interface graphique

Toute l'interface graphique est regroupée dans le fichier `window.py`. Elle a
été réalisée grâce au module `easygui`.

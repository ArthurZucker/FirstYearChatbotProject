#! /usr/bin/env python3

"""
Ce fichier exécute le chatbot en faisant appel aux fonctions des modules se
situant dans le répertoire `source`, à la base de donnés ainsi qu'à
l'ontologie.
"""

from os.path import dirname, realpath
# pour charger l'ontologie
from owlready2 import get_ontology
# pour charger l'interface graphique
from ui import (select_mode_box, image_box, end_box, query_box, cancel_box,
                answer_box)
# pour charger la reponse
from processing import reply
# pour commenter l ontologie
from comment import init_comment

ONTOLOGY_PATH = ("file://" + dirname(dirname(realpath(__file__)))
                 + "/ontology/" + "ontologyGoT.owl")
ONTOLOGY = get_ontology(ONTOLOGY_PATH).load()


def main():
    """
    Main.
    """
    init_comment(ONTOLOGY, ONTOLOGY_PATH)
    answer_list = ["The history:\n\n"]
    still = True
    while still:
        mode = None
        try:
            mode = select_mode_box()
        except AssertionError:
            image_box()
        if mode is None:
            still = end_box()
            continue
        query = query_box(mode)
        if query is None:
            cancel_box()
        else:
            answer, query_found = reply(mode, query, ONTOLOGY)
            if answer is not None:
                result = answer_box(
                    mode,
                    query,
                    query_found,
                    answer,
                    answer_list)
                answer_list.append('\n\n\n'+result)
        still = end_box()


if __name__ == '__main__':
    main()

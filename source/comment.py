"""
Ce fichier contient les fonctions permettant d'interagir avec les commentaires
des propriétés de l'ontologie qui servent à caracteriser les probabilités des
relations.
"""

# pour charger l'ontologie
from owlready2 import comment


def init_comment(ontology, path):
    """
    Cette fonction parcourt l'ensemble des individus, puis l'ensemble de leurs
    propriétés, puis l'ensemble des individus possibles. Une fois l'individu
    n°1, la propriété et l'individu n°2 recuperés, on ajoute un commentaire
    contenant la probabilité de la relations les reliant.

    :param owlready2.namespace.Ontology ontology: l'ontologie.
    """
    properties_names = [p.name for p in list(ontology.object_properties())]
    for individual1 in list(ontology.individuals()):
        data = dir(individual1)
        individual1_properties = []
        for property_name in data:
            if property_name in properties_names:
                property_obj = \
                    ontology.search_one(iri="*" + property_name + "*")
                individual1_properties.append(property_obj)

        if individual1_properties:
            for property_obj in individual1_properties:
                individual2 = individual1.__getattr__(property_obj.name)
                nb_individual = len(individual2)
                if nb_individual > 0:
                    for individual in individual2:
                        comment[individual1, property_obj, individual] = \
                            str(1/nb_individual)
    ontology.save(file=path)


def get_comment(individual1, property_name, individual2, ontology):
    """
    Retourne la probabilité associé à la reliation entre l'individu n°1, la
    propriété et l'individu n°2 dans l'ontologie.

    :param owlready2.entity.ThingClass individual1: l'instance n°1
    :param str property_name: le nom de la propriété.
    :param owlready2.entity.ThingClass individual2: l'instance n°2
    :param owlready2.namespace.Ontology ontology: l'ontologie.
    :return: la probabilité.
    :rtype: str
    """
    property_obj = ontology.search_one(iri="*" + property_name + "*")
    res = str(comment[individual1, property_obj, individual2])
    res = res.replace('[', '')
    res = res.replace(']', '')
    return res

"""
Ce fichier contient les fonctions nécessaires au chatbot pour répondre à la
requête de l'utilisateur grace au parcours sur l'ontologie ou à une base de
données.
"""
import shelve
from textblob import TextBlob

# pour charger l'interface graphique
from ui import not_in_ontology_box, format_error_box, no_result_box
# pour afficher la probabilité
from comment import get_comment


def find_indivdual_by_name(name, ontology):
    """
    Parcourt l'ontologie et récupere l'individu qui a plus de 60% de similitude
    avec le nom veritable.

    :param str name: le nom de l'individu recherché.
    :param owlready2.namespace.Ontology ontology: l'ontologie.
    :return: l'instance correspondant à l'individu ou None si non trouvé.
    :rtype: owlready2.entity.ThingClass ou None
    """
    name = name.strip()
    for individuals in ontology.individuals():
        iterate = 0
        str1 = individuals.name
        str1_len = len(str1)
        name_len = len(name)
        for i in range(min(name_len, str1_len)):
            if str1[i].lower() == name[i].lower():
                iterate = iterate + 1

        percent = (iterate/min(name_len, str1_len))*100
        if percent >= 60:
            return individuals
    return None


def check(mode, raw_query):
    """
    Vérifie si la requête entrée à le bon format eu egard au mode choisi.
    Le format adéquat pour le mode sur une ligne est :
    instance1,propriété,instance2?
    Puis, met la requête sous la forme conventionnelle.

    :param int mode: le mode selectionné : soit 0 (mode une ligne), soit 1
    (mode plusieurs lignes), soit 2 (mode libre).
    :param raw_query: la requête.
    :type raw_query: str ou list(str)
    :return: un couple formé de la requête sous forme de liste(str) et un
        booléen décrivant le mode de saisie.
    :rtype: (list(str) ou None, bool)
    """
    punctuation = {'?', ',', '.', ':', ';'}
    query = None
    if mode == 0:
        if (raw_query.find(',') != -1 and raw_query.find('?') != -1):
            temp_query = raw_query.replace('?', '')
            query = temp_query.split(",")
            indice = 0
        else:
            for letters in raw_query:
                if letters in punctuation:
                    raw_query = raw_query.replace(letters, '')
            query = raw_query
            indice = 1
    elif mode == 1:
        for word in raw_query:
            if word == "":
                return None
        query = raw_query
        indice = 2
    elif mode == 2:
        query = raw_query
        indice = 1
    return query, indice


def is_in_ontology(query, indice, ontology):
    """
    Vérifie la présence des entités recherchées dans l'ontologie.
    Si la requête demandée n'est pas exactement dans l'ontologie, la fonction
    va chercher et renvoyer ce qui correspond à plus 85% a la donnée initiale.
    Retourne un 4-uplet composé de : True si tous les éléments de la requête
    sont dans l'ontologie et False sinon, l'instance du premier terme, le nom
    de la propriété, l'instance du deuxieme terme.

    :param list(str) query: la requête.
    :param bool'indice: le booléen décrivant le mode de saisie.
    :param owlready2.namespace.Ontology ontology: l'ontologie.
    :return: un 4-uplet compose de : True si tous les éléments de la requête
    sont dans l'ontologie et False sinon, l'instance du premier terme, le nom
    de la propriété, l'instance du deuxieme terme. Si l'un des termes n'est pas
    trouvé, il est retourné None à la place.
    :rtype: (bool, owlready2.entity.ThingClass ou None, str ou None,
    owlready2.entity.ThingClass ou None)
    """
    is_in_onto = False
    individual1 = None
    property_name = None
    individual2 = None
    if indice in (0, 2):
        temp_name = query[0].replace("_", " ")
        individual1 = find_indivdual_by_name(temp_name, ontology)
        if individual1 is not None:
            for temp_name in dir(individual1):
                if query[1] == temp_name:
                    property_name = temp_name
                    break
            if property_name is None:
                if query[1].find(" ") == -1:
                    for temp_name in dir(individual1):
                        if temp_name.find(query[1]) != -1:
                            property_name = temp_name
                            break
                else:
                    temp_property_name = query[1].replace(" ", "")
                    property_len = len(temp_property_name)
                    for temp_name in dir(individual1):
                        iterate = 0
                        temp_name_len = len(temp_name)
                        for i in range(min(property_len, temp_name_len)):
                            if (temp_name[i].lower() == temp_property_name[i].
                                    lower()):
                                iterate = iterate + 1
                        percent = iterate/min(property_len, temp_name_len)*100
                        if percent > 85:
                            property_name = temp_name
        if property_name is not None:
            individual2 = find_indivdual_by_name(query[2], ontology)
            is_in_onto = individual2 is not None
        return (is_in_onto, individual1, property_name, individual2)
    # elif indice == 1:
    data = shelve.open('source/basededonnees')
    classifier = data['class']
    data.close()
    blob = TextBlob(query, classifier=classifier)
    return blob


def answer(individual1, property_name, individual2, ontology):
    """
    Rend une réponse binaire a la requête par rapport à l'ontologie, donnée
    sous forme d'instance pour les individus et sous la forme de str pour la
    propriété.

    :param owlready2.entity.ThingClass individual1: l'instance n°1
    :param str property_name: le nom de la propriété.
    :param owlready2.entity.ThingClass individual2: l'instance n°2
    :param owlready2.namespace.Ontology ontology: l'ontologie.
    :return: la réponse à la requête.
    :rtype: str
    """
    if individual2 in individual1.__getattr__(property_name):
        message = "Yes"
    else:
        message = "No"
    message += " (with probability " + get_comment(
        individual1,
        property_name,
        individual2,
        ontology) + ')'
    return message


def reply(mode, raw_query, ontology):
    """
    Si la requête donnée est correcte, retourne la réponse de la requête.

    :param int mode: le mode selectionné soit 0 (mode une ligne) soit 1
        (mode plusieurs lignes).
    :param raw_query: la requête à demander au chatbot.
    :param owlready2.namespace.Ontology ontology: l'ontologie.
    :type raw_query: str ou list(str)
    :return: un couple formé de la réponse de la requête et la requête que le
        chatbot a effectué ou None s'il n'a rien fait.
    :rtype: (str, list(str) ou None)
    """
    query, indice = check(mode, raw_query)
    if indice != 1:
        if query is None:
            format_error_box()
            return None, None
        is_in_onto, individual1, property_name, individual2 = is_in_ontology(
            query,
            indice,
            ontology)
        if is_in_onto:
            response = answer(
                individual1,
                property_name,
                individual2,
                ontology)
            if response is not None:
                query_found = [
                    individual1.name,
                    property_name,
                    individual2.name]
                return response, query_found
            no_result_box()
        not_in_ontology_box()
        return None, None
    bolb = is_in_ontology(query, indice, ontology)
    if bolb.classify() == "pos":
        return ("Yes", query.split())
    return ("No", query.split())

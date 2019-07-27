"""
Ce fichier permet de créer la base de données sur *Game of Thrones* via le
`wiki <gameofthrones.fandom.com/wiki/>`_ necessaire au chatbot.
"""

import shelve
from random import randint
from os.path import dirname, realpath
import requests
from owlready2 import get_ontology
from textblob import TextBlob
from bs4 import BeautifulSoup

ONTOLOGY_PATH = ("file://" + dirname(dirname(realpath(__file__)))
                 + "/ontology/" + "ontologyGoT.owl")
ONTOLOGY = get_ontology(ONTOLOGY_PATH).load()


def generating_url(ontology):
    """
    Generate the url for the ontology.
    """
    url_list = []
    url = "https://gameofthrones.fandom.com/wiki/"
    for individuals in ontology.individuals():
        i = 0
        for char in individuals.name:
            if char == '_':
                i = i + 1
        if i == 1:
            url_list.append(url+individuals.name)
    return url_list


def generating_url2(ontology):
    """
    Generate the url.
    """
    res = []
    url = "https://awoiaf.westeros.org/index.php/"
    for individuals in ontology.individuals():
        i = 0
        for char in individuals.name:
            if char == '_':
                i = i + 1
        if i == 1:
            res.append(url+individuals.name)
    return res


def creation_text(url):
    """
    Create the text.
    """
    cookies = dict(BCPermissionLevel='PERSONAL')
    html = requests.get(
        url,
        cookies=cookies,
        headers={'User-agent': 'Mozilla/5.0'})
    soup = BeautifulSoup(html.content, "html.parser")
    soup.prettify("latin-1")
    soup.encode("ascii", "replace")
    for script in soup(["script", "style"]):
        script.extract()
    text = soup.get_text()
    lines = (line.strip() for line in text.splitlines())
    chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
    text = '\n'.join(chunk for chunk in chunks if chunk)
    for char in text:
        if ord(char) > 127:
            text = text.replace(char, u'')
    return text


def cleaning_text(text):
    """
    Clean the text.
    """
    text_cleaned = ''
    list_temp = []
    for i in range(len(text)):
        # print(words)
        if (i < len(text) - 5) and (text[i:i+5] == '[src]') and not list_temp:
            # cpt = cpt+1
            list_temp.append(i)
            # print("HEY")
        elif ((i < len(text) - 14) and (text[i:i+14] == 'Contents[show]')
              and len(list_temp) == 1):
            list_temp.append(i)
        if len(list_temp) == 2:
            text_cleaned = text[list_temp[0]+6:list_temp[1]-1]
            return text_cleaned
    return text_cleaned


def cleaning_text2(text):
    """
    Clean the text.
    """
    text_cleaned = ''
    list_temp = []
    text_len = len(text)
    for i in range(len(text)):
        # print(words)
        if (i < len(text) - 14) and (text[i:i+14] == 'Contents[show]'):
            text_len = i + 14
        elif (i > text_len) and (text[i:i+6] == 'Season') and not list_temp:
            # cpt = cpt+1
            list_temp.append(i)
            # print("HEY")
        elif ((i > text_len) and (text[i:i+6] == 'Season')
              and (len(list_temp) == 1)):
            list_temp.append(i)
        if len(list_temp) == 2:
            text_cleaned = text[list_temp[0] + 6:list_temp[1] - 1]
            return text_cleaned
    return text_cleaned


def cleaning_text3(text):
    """
    Clean the text.
    """
    text_cleaned = ''
    list_temp = []
    for i in range(len(text)):
        if ((i < len(text) - 8) and (text[i:i+8] == 'Season 8')
                and (not list_temp)):
            list_temp.append(i)
        elif ((i < len(text) - 8) and (text[i:i+8] == 'Contents')
              (len(list_temp) == 1)):
            list_temp.append(i)
        if len(list_temp) == 2:
            text_cleaned = text[list_temp[0] + 9:list_temp[1] - 1]
            return text_cleaned
    return text_cleaned


def cleaning_final(text):
    """
    Clean the text.
    """
    dico = {'them', 'at', 'in', 'for', 'of', 'the', 'and', 'to', 'a', "'s",
            'by', 'though', 'as', 'through', '.', 'is', 'her', 'his', 'into',
            'an', 'that'}
    blob = TextBlob(text)
    # print(blob.words)
    temp = ''
    for line in blob.sentences:
        for words in line.split():
            if words not in dico:
                # print("HAHA")
                # temp.remove(words)
                temp += words + ' '
        temp += '\n'
    return temp


def creation_tabset(text):
    """
    Create the tabset.
    """
    text = text.split('\n')
    res = []
    names = {'Arya', 'Sansa', 'Eddard', 'Ned', 'Jon', 'Danearys', 'Joeffrey',
             'Cersei', 'Hound'}
    passe = True
    # print(text)
    for tokens in text:
        # for char in tokens:
        #     if char in punctuation:
        #         tokens = tokens.replace(char, '')"""
        for words in tokens.split():
            # print(words)
            if words not in names:
                passe = False
            else:
                passe = True
                break
        if tokens != '' and passe is True:
            res.append((tokens, 'pos'))
    # res.append(('', 'neg'))
    return res


def creation_tabset2(text):
    """
    Create the tabset.
    """
    text = text.split('\n')
    res = []
    names = {'Arya', 'Sansa', 'Eddard', 'Ned', 'Jon', 'Danearys', 'Joeffrey',
             'Cersei', 'Hound'}
    passe = True
    for tokens in text:
        # for char in tokens:
        #    if char in punctuation:
        #        tokens = tokens.replace(char, '')"""
        for words in tokens.split():
            if words not in names:
                passe = False
            else:
                passe = True
                break
        if tokens != '' and passe is True:
            temp = randint(0, 10)
            if temp > 4:
                res.append((tokens, 'neg'))
            else:
                res.append((tokens, 'pos'))
    # res.append(('', 'neg'))
    return res


def main():
    """
    Main.
    """
    data = shelve.open('basededonnees')
    classifier = data['class']
    data.close()
    query = input("your question :")
    prob_dist = classifier.prob_classify(query)
    print(round(prob_dist.prob("pos"), 2))


if __name__ == "__main__":
    main()

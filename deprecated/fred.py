#!/usr/bin/env python3

from __future__ import print_function
import fredlib
import time
import sys
sys.path.insert(0, '../python-client/')
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
authorization = '\"Bearer 03c14f7b-9ab2-345a-a1ed-d75c0b314d34\"' # str | The authorization bearear. Type \"Bearer xxx-yyy-zzz\", where is your secret token.
text = 'This is an example' # str | The input natural language text.
prefix = 'GoT' # str | The prefix used for the namespace of terms introduced by FRED in the output. If not specified fred: is used as default. (optional)
namespace = 'namespace_example' # str | The namespace used for the terms introduced by FRED in the output. If not specified http://www.ontologydesignpatterns.org/ont/fred/domain.owl# is used as default. (optional)
wsd = True # bool | Perform Word Sense Disambiguation on input terms. By default it is set to false. (optional)
wfd = True # bool | Perform Word Frame Disambiguation on input terms in order to provide alignments to WordNet synsets, WordNet Super-senses and Dolce classes. By default it is set to false. (optional)
wfd_profile = 'b' # str | The profile associated with the Word Frame Disambiguation (optional) (default to b)
tense = True # bool | Include temporal relations between events according to their grammatical tense. By default it is set to false. (optional)
roles = True # bool | Use FrameNet roles into the resulting ontology. By default it is set to false. (optional)
textannotation = 'earmark' # str | The vocabulary used for annotating the text in RDF. Two possible alternatives are available, i.e. EARMARK and NIF. (optional) (default to earmark)
semantic_subgraph = True # bool | Generate a RDF which only expresses the semantics of a sentence without additional RDF triples, such as those containing text spans, part-of-speeches, etc. By default it is set to false. (optional)

try:
    api_instance.stlab_tools_fred_get(authorization, text, prefix=prefix, namespace=namespace, wsd=wsd, wfd=wfd, wfd_profile=wfd_profile, tense=tense, roles=roles, textannotation=textannotation, semantic_subgraph=semantic_subgraph)
except ApiException as e:
    print("Exception when calling DefaultApi->stlab_tools_fred_get: %s\n" % e)

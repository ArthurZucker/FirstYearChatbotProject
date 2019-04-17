#from __future__ import print_statement
import fredlibs
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
text = text_example # String | The input natural language text.
prefix = prefix_example # String | The prefix used for the namespace of terms introduced by FRED in the output. If not specified fred: is used as default. (optional)
namespace = namespace_example # String | The namespace used for the terms introduced by FRED in the output. If not specified http://www.ontologydesignpatterns.org/ont/fred/domain.owl# is used as default. (optional)
wsd = true # Boolean | Perform Word Sense Disambiguation on input terms. By default it is set to false. (optional)
wfd = true # Boolean | Perform Word Frame Disambiguation on input terms in order to provide alignments to WordNet synsets, WordNet Super-senses and Dolce classes. By default it is set to false. (optional)
wfdProfile = wfdProfile_example # String | The profile associated with the Word Frame Disambiguation (optional) (default to b)
tense = true # Boolean | Include temporal relations between events according to their grammatical tense. By default it is set to false. (optional)
roles = true # Boolean | Use FrameNet roles into the resulting ontology. By default it is set to false. (optional)
textannotation = textannotation_example # String | The vocabulary used for annotating the text in RDF. Two possible alternatives are available, i.e. EARMARK and NIF. (optional) (default to earmark)
semanticSubgraph = true # Boolean | Generate a RDF which only expresses the semantics of a sentence without additional RDF triples, such as those containing text spans, part-of-speeches, etc. By default it is set to false. (optional)

try:
    api_instance.stlabToolsFredGet(text, prefix=prefix, namespace=namespace, wsd=wsd, wfd=wfd, wfdProfile=wfdProfile, tense=tense, roles=roles, textannotation=textannotation, semanticSubgraph=semanticSubgraph)
except ApiException as e:
    print("Exception when calling DefaultApi->stlabToolsFredGet: %s\n" % e)

import connexion
import six

from swagger_server import util


def stlab_tools_fred_get(Authorization, text, prefix=None, namespace=None, wsd=None, wfd=None, wfd_profile=None, tense=None, roles=None, textannotation=None, semantic_subgraph=None):  # noqa: E501
    """stlab_tools_fred_get

    Generate RDF from natural language text. # noqa: E501

    :param Authorization: The authorization bearear. Type \&quot;Bearer xxx-yyy-zzz\&quot;, where is your secret token.
    :type Authorization: str
    :param text: The input natural language text.
    :type text: str
    :param prefix: The prefix used for the namespace of terms introduced by FRED in the output. If not specified fred: is used as default.
    :type prefix: str
    :param namespace: The namespace used for the terms introduced by FRED in the output. If not specified http://www.ontologydesignpatterns.org/ont/fred/domain.owl# is used as default.
    :type namespace: str
    :param wsd: Perform Word Sense Disambiguation on input terms. By default it is set to false.
    :type wsd: bool
    :param wfd: Perform Word Frame Disambiguation on input terms in order to provide alignments to WordNet synsets, WordNet Super-senses and Dolce classes. By default it is set to false.
    :type wfd: bool
    :param wfd_profile: The profile associated with the Word Frame Disambiguation
    :type wfd_profile: str
    :param tense: Include temporal relations between events according to their grammatical tense. By default it is set to false.
    :type tense: bool
    :param roles: Use FrameNet roles into the resulting ontology. By default it is set to false.
    :type roles: bool
    :param textannotation: The vocabulary used for annotating the text in RDF. Two possible alternatives are available, i.e. EARMARK and NIF.
    :type textannotation: str
    :param semantic_subgraph: Generate a RDF which only expresses the semantics of a sentence without additional RDF triples, such as those containing text spans, part-of-speeches, etc. By default it is set to false.
    :type semantic_subgraph: bool

    :rtype: None
    """
    return 'do some magic!'

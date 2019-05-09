# swagger_client.DefaultApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**stlab_tools_fred_get**](DefaultApi.md#stlab_tools_fred_get) | **GET** /stlab-tools/fred | 


# **stlab_tools_fred_get**
> stlab_tools_fred_get(authorization, text, prefix=prefix, namespace=namespace, wsd=wsd, wfd=wfd, wfd_profile=wfd_profile, tense=tense, roles=roles, textannotation=textannotation, semantic_subgraph=semantic_subgraph)



Generate RDF from natural language text.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
authorization = 'authorization_example' # str | The authorization bearear. Type \"Bearer xxx-yyy-zzz\", where is your secret token.
text = 'text_example' # str | The input natural language text.
prefix = 'prefix_example' # str | The prefix used for the namespace of terms introduced by FRED in the output. If not specified fred: is used as default. (optional)
namespace = 'namespace_example' # str | The namespace used for the terms introduced by FRED in the output. If not specified http://www.ontologydesignpatterns.org/ont/fred/domain.owl# is used as default. (optional)
wsd = true # bool | Perform Word Sense Disambiguation on input terms. By default it is set to false. (optional)
wfd = true # bool | Perform Word Frame Disambiguation on input terms in order to provide alignments to WordNet synsets, WordNet Super-senses and Dolce classes. By default it is set to false. (optional)
wfd_profile = 'b' # str | The profile associated with the Word Frame Disambiguation (optional) (default to b)
tense = true # bool | Include temporal relations between events according to their grammatical tense. By default it is set to false. (optional)
roles = true # bool | Use FrameNet roles into the resulting ontology. By default it is set to false. (optional)
textannotation = 'earmark' # str | The vocabulary used for annotating the text in RDF. Two possible alternatives are available, i.e. EARMARK and NIF. (optional) (default to earmark)
semantic_subgraph = true # bool | Generate a RDF which only expresses the semantics of a sentence without additional RDF triples, such as those containing text spans, part-of-speeches, etc. By default it is set to false. (optional)

try:
    api_instance.stlab_tools_fred_get(authorization, text, prefix=prefix, namespace=namespace, wsd=wsd, wfd=wfd, wfd_profile=wfd_profile, tense=tense, roles=roles, textannotation=textannotation, semantic_subgraph=semantic_subgraph)
except ApiException as e:
    print("Exception when calling DefaultApi->stlab_tools_fred_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| The authorization bearear. Type \&quot;Bearer xxx-yyy-zzz\&quot;, where is your secret token. | 
 **text** | **str**| The input natural language text. | 
 **prefix** | **str**| The prefix used for the namespace of terms introduced by FRED in the output. If not specified fred: is used as default. | [optional] 
 **namespace** | **str**| The namespace used for the terms introduced by FRED in the output. If not specified http://www.ontologydesignpatterns.org/ont/fred/domain.owl# is used as default. | [optional] 
 **wsd** | **bool**| Perform Word Sense Disambiguation on input terms. By default it is set to false. | [optional] 
 **wfd** | **bool**| Perform Word Frame Disambiguation on input terms in order to provide alignments to WordNet synsets, WordNet Super-senses and Dolce classes. By default it is set to false. | [optional] 
 **wfd_profile** | **str**| The profile associated with the Word Frame Disambiguation | [optional] [default to b]
 **tense** | **bool**| Include temporal relations between events according to their grammatical tense. By default it is set to false. | [optional] 
 **roles** | **bool**| Use FrameNet roles into the resulting ontology. By default it is set to false. | [optional] 
 **textannotation** | **str**| The vocabulary used for annotating the text in RDF. Two possible alternatives are available, i.e. EARMARK and NIF. | [optional] [default to earmark]
 **semantic_subgraph** | **bool**| Generate a RDF which only expresses the semantics of a sentence without additional RDF triples, such as those containing text spans, part-of-speeches, etc. By default it is set to false. | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/rdf+xml, text/turtle, application/rdf+json, text/rdf+n3, text/rdf+nt, image/png

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


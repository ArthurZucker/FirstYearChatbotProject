import nltk
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')

document = "Jon Snow, born Aegon Targaryen, is the son of Lyanna Stark and Rhaegar Targaryen, the late Prince of Dragonstone. From infancy, Jon is presented as the bastard son of Lord Eddard Stark, Lyanna's brother, and raised by Eddard alongside his lawful children of House Stark at Winterfell, but his true parentage is kept secret from everyone, including Jon himself, in order to protect him from those that sought the complete annihilation of House Targaryen after Robert's Rebellion and to maintain order in the realm."



def ie_preprocess(document):
   sentences = nltk.sent_tokenize(document)
   sentences = [nltk.word_tokenize(sent) for sent in sentences]
   sentences = [nltk.pos_tag(sent) for sent in sentences] 
   return sentences

print(ie_preprocess(document)[0])

grammar = r"""
  NP: {<DT|PP\$>?<JJ>*<NN>}   
      {<NNP>+}       
  """         
cp = nltk.RegexpParser(grammar)

print(cp.parse(ie_preprocess(document)[0]))
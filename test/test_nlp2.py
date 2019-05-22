from textblob import TextBlob
from bs4 import BeautifulSoup
import urllib.request
from textblob import classifiers

"""response =  urllib.request.urlopen('https://gameofthrones.fandom.com/wiki/Jon_Snow')
html = response.read()
soup = BeautifulSoup(html,'html5lib')
text = soup.get_text(strip = True)
"""
punctuation = ['.', '!', ';']
blob = TextBlob("Jon Snow, born Aegon Targaryen, is the son of Lyanna Stark and Rhaegar Targaryen, the late Prince of Dragonstone. From infancy, Jon is presented as the bastard son of Lord Eddard Stark, Lyanna's brother, and raised by Eddard alongside his lawful children of House Stark at Winterfell, but his true parentage is kept secret from everyone, including Jon himself, in order to protect him from those that sought the complete annihilation of House Targaryen after Robert's Rebellion and to maintain order in the realm.")
test_text = "Jon Snow, born Aegon Targaryen, is the son of Lyanna Stark and Rhaegar Targaryen, the late Prince of Dragonstone. From infancy, Jon is presented as the bastard son of Lord Eddard Stark, Lyanna's brother, and raised by Eddard alongside his lawful children of House Stark at Winterfell, but his true parentage is kept secret from everyone, including Jon himself, in order to protect him from those that sought the complete annihilation of House Targaryen after Robert's Rebellion and to maintain order in the realm."
test_text = test_text.split('.')
L = []
for tokens in test_text:
	"""for c in tokens:
		if c in punctuation:
			tokens = tokens.replace(c, '')"""
	if tokens != '':
		L.append((tokens, 'pos'))
#print(L)
"""for np in blob.noun_phrases:
 print (np)

for ngram in blob.ngrams(2):
	print (ngram)"""
"""L = list()
L.append("Jon Snow, born Aegon Targaryen, is the son of Lyanna Stark and Rhaegar Targaryen", "pos")"""

training = [
('Jon Snow, is the son of Lyanna Stark and Rhaegar Targaryen','pos'),
('Jon Snow is born Aegon Targaryen.','pos'),
('Jon Snow is the bastard son of Ned Stark','neg'),
('Jon Snow is from the Night\s watch','pos'),
('Jon Snow has a wife','neg'),
('Jon Snow is a Stark','pos'),
('Jon Snow loves Dragonstone', 'pos'),
('Jon Snow knows something', 'neg')
]
L.append((' ','neg'))
testing = [
('Jon Snow is a bastard','neg'),
('Jon Snow lives at Dragonstone','pos'),
('Jon Snow has a son','neg')
]


classifier = classifiers.NaiveBayesClassifier(training)
#classifier.show_informative_features(3)
prob_dist = classifier.prob_classify("?")
print(round(prob_dist.prob("pos"), 2))

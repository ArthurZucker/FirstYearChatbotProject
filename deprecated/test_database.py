
# L_tab = []
#
# for url in L:
# 	text = creation_text(url)
# 	text_cleaned2 = cleaning_text2(text)
# 	text_cleaned2 = cleaning_final(text_cleaned2)
# 	text_cleaned = cleaning_text(text)
# 	text_cleaned = cleaning_final(text_cleaned)
# 	L_tab = L_tab + creation_tabset(text_cleaned) + creation_tabset2(text_cleaned2)
# #print(text_cleaned)
# print(L_tab)
#
# L2 = generating_url2(ontology)
#
#
# print(L_tab)
#
# for url in L2:
# 	text = creation_text(url)
# 	text_cleaned = cleaning_text3(text)
# 	text_cleaned = cleaning_final(text_cleaned)
# 	L_tab = L_tab + creation_tabset(text_cleaned)
#
# classifier = classifiers.NaiveBayesClassifier(L_tab)

L = generating_url(ontology)
L2 = generating_url2(ontology)

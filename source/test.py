
D = {"loyal":"isLoyalTo"}

sentence = "Arya, is loyal to, Sansa ?"

sentence = sentence.split(",")

s2 = sentence[1].split(" ")

print(s2)

print(sentence[1])

for words in s2:
	if words in D:
		#print(words)
		sentence[1] = sentence[1].replace(words, D[words])
	else:
		sentence[1] = sentence[1].replace(words, "")

print(sentence[1])
#print(D["loyal"])
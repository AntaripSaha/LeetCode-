from collections import Counter
word1 = "abbzzca"
word2 = "babzzcz"
word1_set = set(word1)
word2_set = set(word2)
frequencies1 = Counter(word1)
frequencies2 = Counter(word2)

if (word1_set == word2_set
    and len(word1) == len(word2)
    and sorted(frequencies1.values()) == sorted(frequencies2.values())):
    print('True')
else:
    print('False')

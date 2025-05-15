word1 = "abcd"
word2 = "pqr"
i = 0
pointer2 = 0
result = []
while i<len(word1) and pointer2<len(word2):
    result.append(word1[i])
    result.append(word2[pointer2])
    i += 1
    pointer2 += 1
result += word1[i:]
result += word2[pointer2:]
print("".join(result))

strs = ["neet","code","love","you"]

result = ""

# encoding
for s in strs:
    # print(len(s))
    result += str(len(s)) + "$" + s
print(result)

# decoding
# print(result[0:1])

res = []
i = 0
s = result
while i<len(s):
    j = i
    while s[j] != '$':
        j += 1
    length = int(s[i:j])
    i = j + 1
    j = i + length
    res.append(s[i:j])
    i = j
print(res)


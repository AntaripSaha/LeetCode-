s = "aedciiidef"
k = 3
vowels = set("aeiou")
count = 0
for i in s[:k]:
    if i in vowels:
        count += 1
result = count
for ch in range(k, len(s)):
    if s[ch-k] in vowels:
        count -= 1
    if s[ch] in vowels:
        count += 1
    result = max(result, count)

print(result)
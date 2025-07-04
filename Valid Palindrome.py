s = "Was it a car or a cat I saw?"

newString = ''

for c in s:
    if c.isalnum():
        newString += c.lower()
print(newString == newString[::-1])
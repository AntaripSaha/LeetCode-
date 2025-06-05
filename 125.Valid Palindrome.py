s = "A man, a plan, a canal: Panama"
s = s.lower()
cleaned = ""
for c in s:
    if c.isalnum():
        cleaned += c
print(cleaned == cleaned[::-1])

# we will lowercase the string
# if its a alphanumeric Char, we will store and check with reverse
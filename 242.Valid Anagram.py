from collections import Counter

s = "anagram"
t = "nagaram"

if Counter(s) == Counter(t):
    print("True")
else:
    print("False")

# counter counts the elements
# Counter({'a': 3, 'n': 2, 'b': 1})
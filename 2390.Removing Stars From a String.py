s = "leet**cod*e"
result = []

for char in s:
    if char != '*':
        result.append(char)
    else:
        result.pop()

print("".join(result))

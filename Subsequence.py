s = "abc"
t = "ahbgdc"
i = 0 # t pointer
j = 0 # s pointer
# count = 0
while i<len(t):
    if j<len(s) and s[j] == t[i]:
        # count += 1
        j += 1
    i+=1

# if count == len(s):
#     print('True')
# else:
#     print('False')

print(j==len(s))
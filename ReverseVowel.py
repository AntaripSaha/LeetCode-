s = "ai"
s_list = list(s)
i = 0 # start Pointer
j = len(s)-1 #end pointer
vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}

while i<j:
    if s_list[i] in vowels and s_list[j] in vowels:
        s_list[i], s_list[j] = s_list[j], s_list[i]
        i += 1
        j -= 1
    elif s_list[i] not in vowels:
        i += 1
    else:
        j -= 1

print("".join(s_list))
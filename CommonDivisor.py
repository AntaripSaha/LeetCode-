import  math
str1 = "ABCABC"
str2 = "CODEddAA"

if str1 + str2 != str2 + str1:
    print('""')
else:
    gcd_length = math.gcd(len(str1), len(str2))
    print(str1[:gcd_length])






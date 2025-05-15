gain = [-4,-3,-2,-1,4,3,2]

temp = 0
max_value = 0
i = 0
while i<len(gain):
    temp += gain[i]
    max_value = max(temp, max_value)
    i+=1
print(max_value)
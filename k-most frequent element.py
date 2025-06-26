nums = [1,2,2,3,3,3]
k = 2
frq_map = {}
result = []

for num in nums:
    frq_map[num] = frq_map.get(num, 0) + 1
print(frq_map)

sorted_items = sorted(frq_map.items(), key=lambda item: item[1], reverse=True)
print(sorted_items)
for i in range(k):
    number = sorted_items[i][0]
    result.append(number)

print(result)
height = [1,8,6,2,5,4,8,3,7]
result = float('-inf')
i = 0
j = len(height)-1
while i<j:
    area = min(height[i], height[j]) * (j - i)
    result = max(result, area)
    if height[i]<height[j]:
        i += 1
    else:
        j -= 1
print(result)



nums  = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1]
k = 3
left = 0
right = 0
count = 0
result = 0

while right<len(nums):
    if nums[right] == 0:
        count += 1
    while count>k:
        if nums[left] == 0:
            count -= 1
        left += 1
    result = max(result, (right - left) + 1)
    right += 1

print(result)


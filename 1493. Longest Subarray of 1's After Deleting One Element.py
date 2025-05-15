nums = [0,1,1,1,0,1,1,0,1]
left = 0
right = 0
zero_count = 0
result = 0

while right < len(nums):
    if nums[right] == 0:
        zero_count += 1
    while zero_count>1:
        if nums[left] == 0:
            zero_count -= 1
        left += 1
    result = max(result, right - left)
    right += 1

print(result)
nums = [0,1,2,2,3,0,4,2]
val = 2
k = 0
for num in range(len(nums)):
    # print(num)
    if nums[num] != val:
        nums[k] = nums[num]
        k += 1

print(k)
nums = [2,1]
i = 0 #slow pointer
j = 1 #fast pointer

for j in range(len(nums)):
    if nums[j] != 0:
        nums[i], nums[j] = nums[j], nums[i]
        i +=1
        j +=1
    else:
        j +=1
print(nums)



nums = [4,4,1,3,1,3,2,2,5,5,1,5,2,1,2,3,5,4]
k = 5
nums.sort()
count = 0
i = 0 #first pointer
j = len(nums)-1 #last pointer

while i<j:
    if nums[i]+nums[j] == k:
        count += 1
        i += 1
        j -= 1
    elif nums[i]+nums[j]<k:
        i += 1
    else:
        j -= 1
print(count)

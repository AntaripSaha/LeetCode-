nums = [-1,0,1,2,-1,-4]
nums = sorted(nums)
ans = []

for i, num in enumerate(nums):
    if i>0 and nums[i] == nums[i-1]:
        continue
    j = i+1
    k = len(nums)-1
    while j<k:
        sum = nums[i] + nums[j] + nums[k]
        if sum<0:
            j += 1
        elif sum>0:
            k -= 1
        else:
            ans.append([nums[i], nums[j], nums[k]])
            j += 1
            while nums[j] == nums[j-1] and j<k:
                j += 1

print(ans)
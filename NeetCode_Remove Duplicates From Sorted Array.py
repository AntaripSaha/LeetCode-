
nums = [2,10,10,30,30,30]
l = 1
for r in range(1, len(nums)):
    if nums[r] != nums[r - 1]:
        nums[l] = nums[r]
        l += 1
print(nums)
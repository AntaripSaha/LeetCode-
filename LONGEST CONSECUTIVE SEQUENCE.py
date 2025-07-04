nums = [0,3,2,5,4,6,1,1]

numSet = set(nums)
print(numSet)
longest = 0
for n in nums:
    if (n-1) not in numSet:
        length = 0
        while (n+length) in numSet:
            length += 1
        longest = max(longest, length)
print(longest)
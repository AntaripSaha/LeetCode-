nums = [1,2,3,4]
answer = [1]*len(nums)
n = len(nums)

prefix = 1
for i in range(len(nums)):
    answer[i] *= prefix
    prefix *= nums[i]

suffix = 1
for i in range(n-1, -1, -1):
    answer[i] *= suffix
    suffix *= nums[i]

print(answer)

# prefix suffix

# nums = [1, 2, 3, 4]
# n = len(nums)
# 
# prefix = [1] * n
# suffix = [1] * n
#
# for i in range(1, n):
#     prefix[i] = prefix[i - 1] * nums[i - 1]
#
# for i in range(n - 2, -1, -1):
#     suffix[i] = suffix[i + 1] * nums[i + 1]
#
# print("Prefix:", prefix)
# print("Suffix:", suffix)

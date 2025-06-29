# nums = [1,2,3,4]

# res = [1]*len(nums)
# for i in range(len(nums)):
#     j = 0
#     while j<len(nums):
#         if i != j:
#             res[i] *= nums[j]
#         j+= 1
#
# print(res)


# n = len(nums)
# result = [1] * n
# for i in range(n):
#     product = 1
#     for j in range(n):
#         if i != j:
#             product *= nums[j]
#     result[i] = product
# print(result)


# with prefix and suffix

#prefix

nums = [1,2,3,4]
n = len(nums)
suffix = 1
answer = [1]*n
print(answer)
for i in range(1, n):
    answer[i] = answer[i-1] * nums[i-1]
print(answer)
for i in range(n-2, -1, -1):
    suffix *= nums[i+1]
    answer[i] *= suffix




print(answer)




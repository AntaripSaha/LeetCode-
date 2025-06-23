# nums = [2,7,11,15]
# target = 17
# map = {}
# for i, num in enumerate(nums):
#     complement = target - num
#     if complement in map:
#         print([map[complement], i])
#     map[num] = i
# we will calculate which amount is left,
# if we see the left amount in future then that will be the ans


#updated NeetCode

nums = [3,4,5,6]
target = 7
result = {} # hash map: value---index
for i,n in enumerate(nums):
    new_value = target - n
    if new_value in result:
        print([result[new_value], i])
    result[n] = i























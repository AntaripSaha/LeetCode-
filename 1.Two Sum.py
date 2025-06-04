nums = [2,7,11,15]
target = 17
map = {}
for i, num in enumerate(nums):
    complement = target - num
    if complement in map:
        print([map[complement], i])
    map[num] = i
# we will calculate which amount is left,
# if we see the left amount in future then that will be the ans
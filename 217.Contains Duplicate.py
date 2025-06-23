# nums = [1,2,3,1]
# seen = set()
#
# for num in nums:
#     if num in seen:
#         print("True")
#         exit()
#     else:
#         seen.add(num)
# print("False")

# python set, it keeps the unique values,
# if we don't see any common value then we will add it to the set,

# updated
nums = [1, 2, 3, 3]

seen = set()

for num in nums:
    if num != seen:
        seen.add(num)

print(len(nums) != len(seen))























# nums = [2,1,5,0,4,6]
# first = float('inf')
# second = float('inf')
# for i in nums:
#     if i<= first:
#         first = i
#     elif i<= second:
#         second = i
#     else:
#         print('true')
#         exit()
#
# print('false')
#
nums = [0, 1, 0, 3, 2, 3]
count = 0
check = float('inf')
for num in nums:
    if num<=check:
        check = num
        count +=1
print(count)



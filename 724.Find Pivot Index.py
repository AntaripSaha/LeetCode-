nums = [1,7,3,6,5,6]
left_sum = 0
right_sum = 0
total_sum = sum(nums)

for i in range(len(nums)):
    right_sum = total_sum - left_sum - nums[i]
    if left_sum == right_sum:
        print(i)
        exit()
    left_sum += nums[i]
    # print(left_sum)

print(-1)
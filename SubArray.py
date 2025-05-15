nums = [5,4,4,5,3,2,1,2,5]
k = 3
window_sum = sum(nums[:k])
result = window_sum/k
for i in range(k, len(nums)):
    window_sum = window_sum - nums[i-k] + nums[i]
    average = window_sum/k
    # if average>result:
    #     result = average
    result = max(result, average)

print(result)

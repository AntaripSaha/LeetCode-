numbers = [1,2,3,4]
target = 3
l = 0
r = len(numbers)-1
while l<r:
    sum = numbers[l] + numbers[r]
    if sum > target:
        r -=1
    elif sum < target:
        l += 1
    else:
        print([l+1, r+1])
        exit()

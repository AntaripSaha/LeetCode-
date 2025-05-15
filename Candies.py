candies = [2,3,5,1,3]
extraCandies = 3
result = [False] * len(candies)
maxKids = max(candies)

for i, candy in enumerate(candies):
    if  candy + extraCandies >= maxKids:
        result[i] = "true"
    else:
        result[i] = "false"

print(result)
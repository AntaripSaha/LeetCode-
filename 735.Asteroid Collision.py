asteroids = [-2,-2,1,-2] #[-2,-1,1,2]
result = []

for value in asteroids:
    if value > 0:
        result.append(value)
    else:
        while result and result[-1] > 0:
            if abs(value) > result[-1]:
                result.pop()
                continue
            elif abs(value) == result[-1]:
                result.pop()
            break
        else:
            result.append(value)



print(result)

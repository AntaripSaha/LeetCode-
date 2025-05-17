grid = [[3,2,1],[1,7,6],[2,7,7]]
columns = list(zip(*grid))
count = 0
for row in grid:
    for column in columns:
        if row == list(column):
            count += 1

print(count)

print('row: ', grid)
print('col: ', list(columns))

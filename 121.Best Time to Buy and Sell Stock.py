prices = [7,2,5,1,3,6,4,8]
min_price = float('inf')
max_profit = 0
for price in prices:
    if price < min_price:
        min_price = price
    else:
        profit = (price - min_price)
        max_profit = max(max_profit, profit)
print(max_profit)

# when we will see the minimum value, we will store it in min_price
# then we will calculate the maximum profit with respect to min_price

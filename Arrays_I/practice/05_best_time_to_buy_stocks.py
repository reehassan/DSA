# arrays(list)
prices = [32,43,55,30,90,85]
# index=  0  1  2  3  4  5
# day  =  1  2  3  4  5  6

# printing 
# print(prices[2])

# looping to get value
# for price in prices:
#     print(price)

# looping to get index and value together
highest = 0
for i in prices:
    # print(i, prices[i])
    if i > highest:
        highest = i
print(highest)

lowest = 90
for i in prices:
    if i < lowest:
        lowest = i
print(lowest)


# 1. Set minimum_price = prices[0]

# 2. Set maximum_profit = 0

# 3. For every price in prices starting from index 1:

#     a. profit = current_price - minimum_price

#     b. If profit > maximum_profit:
#            maximum_profit = profit

#     c. If current_price < minimum_price:
#            minimum_price = current_price

# 4. Return maximum_profit
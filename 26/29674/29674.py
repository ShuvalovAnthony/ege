f = open('26/29674/29674.txt')

summa = 0
prices = []

for i in f:
    num = int(i)
    if num <= 50: summa += num
    else: prices.append(num)

prices = sorted(prices)

for i in range(len(prices)//2):
    summa += prices[i]*0.75 + prices[len(prices) - i - 1]

print(round(summa), prices[len(prices)//2 - 1])



# Способ 2
# f = open('26/29674/29674.txt')

# summa = 0
# prices = []

# for i in f:
#     num = int(i)
#     if num <= 50: summa += num
#     else: prices.append(num)

# prices = sorted(prices)

# low_prices = prices[:len(prices)//2]
# high_prices = prices[len(prices)//2::]

# summa += sum(low_prices)*0.75 + sum(high_prices)

# print(round(summa), low_prices[-1])
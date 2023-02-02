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

print(int(summa), prices[len(prices)//2 - 1])
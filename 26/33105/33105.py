f = open('26/33105/inf_22_10_20_26.txt')

n = int(f.readline())


itog_summa = 0

prices = [] # список товаров дороже 100 рублей

for i in f:
    price = int(i)
    if price <= 100:
        itog_summa += price
    else:
        prices.append(price)

prices = sorted(prices)

if len(prices)%2 == 0:
    prices_skidka = prices[:len(prices)//2]
    prices_bez_skidki = prices[len(prices)//2:]
else:
    itog_summa += prices[len(prices)//2]
    prices_skidka = prices[:len(prices)//2]
    prices_bez_skidki = prices[len(prices)//2 + 1:]


itog_summa += sum(prices_skidka)*0.7 + sum(prices_bez_skidki)

print(itog_summa, prices_skidka[-1])

# 459 678
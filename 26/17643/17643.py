f = open("ege/26/17643/26_17643.txt")

k = int(f.readline())

temp_goods = []

prices = set()


for row in f:
    art, price, status = (int(i) for i in row.split())
    prices.add(price)
    temp_goods.append([art, price, status])

avg = sum(prices)/len(prices)

goods = []

for item in temp_goods:
    if item[1] > avg:
        goods.append(item)


# art: [price, sold, least]
total = {}


for item in goods:
    art = item[0]
    if art in total:
        price, sold, least = total[art]
        if not item[2]:
            sold += 1
        else:
            least += 1
        total[art] = [price, sold, least]
    else:
        price = item[1]
        sold = item[2]
        total[art] = [price, 0 if sold else 1, 1 if sold else 0]


#  [art, price, sold, least]
total_list = []

for art, data in total.items():
    total_list.append([art, *data])


total_list = sorted(total_list, key=lambda x: (
    -x[2],
    -x[1],
    x[3]
))


# for row in total_list:
#     print(row)

best_good = total_list[0]
print(best_good)
price, sold, least = best_good[1:]

print(price*sold, least)



f = open('26/6641/26_6641.txt')

n, money = map(int, f.readline().split())
w_goods = []
s_goods = []

for i in f:
    price, type = i.split()
    if type == 'S': s_goods.append(int(price))
    else: w_goods.append(int(price))



w_goods, s_goods = sorted(w_goods), sorted(s_goods)

answ = []


for i in range(len(s_goods)): 
    diff = money - sum(s_goods[:i])
    if diff < 0:
        print(i)
        break


for s in range(700):
    for w in range(700):
        s_money = sum(s_goods[:s])
        w_money = sum(w_goods[:w])
        if s_money + w_money <= money:
            answ.append(
                [
                s + w,
                s,
                money - s_money - w_money
                ]
            )

print(max(answ))
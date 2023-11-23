f = open('26/38960/26.txt')

n, money = [int(i) for i in f.readline().split()]

a_izd, b_izd = [], []

for i in f:
    row = i.split()
    if row[-1] == 'A': a_izd.append(int(row[0]))
    else: b_izd.append(int(row[0]))


a_izd, b_izd = sorted(a_izd), sorted(b_izd)
all_izd = sorted(a_izd + b_izd)


max_counter = 0
temp_money = money
for price in all_izd:
    if temp_money - price >= 0:
        max_counter += 1
        temp_money -= price


for i in range(max_counter, 0, -1):
    
    summa_a = sum(a_izd[:i])
    summa_b = sum(b_izd[:max_counter - i])
    if (
        summa_a + summa_b < money
    ):
        print(i, money - summa_a - summa_b)
        break

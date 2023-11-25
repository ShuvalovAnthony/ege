from itertools import product

counter = 0
answ = []
for i in product([0, 1], repeat=6):
    if (
        ((((i[0] <= i[1]) <= i[2]) <= i[3]) <= i[4]) <= i[5]
    ):
        s = ''.join([str(i[0]), str(i[1]), str(i[2]), str(i[3]), str(i[4]), str(i[5])])
        answ.append(s)
        counter += 1

print(counter)
for i in sorted(answ):
    print(i)
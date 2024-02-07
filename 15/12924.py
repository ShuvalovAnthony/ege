from itertools import combinations

p = {i for i in range(2, 21, 2)}
q = {i for i in range(3, 31, 3)}


a = p|q # ob'ed dvuh mnozhestv

sets_a = []

for i in range(1, len(a) + 1):
    for set_a in combinations(a, i):
        sets_a.append(set_a)


for set_a in sets_a[::-1]:
    flag = True

    for x in a:
        if not (
            (
                (x in set_a) <= (x in p)
            ) and
            (
                (x not in q) <=
                (x not in set_a)
            )
        ):
            flag = False
            break

    if flag:
        print(len(set_a))
        break

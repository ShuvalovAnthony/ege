def treug(n, m, k):
    sides = sorted([n, m, k])
    return sides[0] + sides[1] > sides[2]


# range() для А и для Х - одинаковый ?????!!!!!

for a in range(1, 1000):
    flag = True
    for x in range(1, 1000):
        if not (
            not (treug(x,11,16) == ((not(max(x,5) > 10))) and treug(4,a,x))
        ):
            flag = False
            break


    if flag:
        print(a)
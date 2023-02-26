from itertools import combinations


def p(x):
    return 35 <= x <= 55

def q(x):
    return 45 <= x <= 65

def a(x, start, stop):
    return start <= x <= stop

coords = combinations(
    sorted([65, 55, 35, 45]),
    2,
)

dlini = [] # ntf

for start, stop in coords:
    flag = True

    for x in range(0, 100):
        if ((p(x) <= a(x, start, stop)) and \
            ((not a(x, start, stop)) <= (not q(x)))) == False:
            flag = False
            break

    if flag == True:
        dlini.append(stop - start)


print(dlini, min(dlini))
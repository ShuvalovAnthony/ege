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

min_dlina = 10**6

for start, stop in coords:
    flag = True

    for x in range(0, 100):
        if ((p(x) <= a(x, start, stop)) and \
            ((not a(x, start, stop)) <= (not q(x)))) == False:
            flag = False
            break

    if flag == True:
        min_dlina = min(min_dlina, stop - start)


print(min_dlina)
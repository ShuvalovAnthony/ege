from itertools import combinations

def p(x):
    return 30 <= x <= 45

def q(x):
    return 40 <= x <= 55

def a(start, stop, x):
    return start <= x <= stop


coords = combinations([30, 40, 45, 55], 2)

min_dlina = 10**6

for start, stop in coords:
    flag = True

    for x in range(0, 100):
        if (
            (not ((not a(start, stop, x)) <= (not p(x)))) or
            (not (q(x) <= a(start, stop, x)))
        ):
            flag = False
            break

    if flag:
        min_dlina = min(min_dlina, stop - start)


print(min_dlina)
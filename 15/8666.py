from itertools import combinations

def p(x):
    return 25 <= x <= 50

def q(x):
    return 32 <= x <= 47

def a(start, stop, x):
    return start <= x <= stop


coords = combinations([25, 32, 47, 50], 2)

dlini = []

for start, stop in coords:
    flag = True
    
    for x in range(0, 100):
        if not (
            ((not (a(start, stop, x))) <= p(x)) <= (a(start, stop, x) <= q(x))
            ):
            flag = False
            break

    if flag:
        max_dlina = dlini.append(stop - start)

print(dlini)
print(max(dlini))



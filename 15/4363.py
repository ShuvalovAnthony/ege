from itertools import combinations


def a(x): return 30 <= x <= 50

def p(x): return 10<= x <= 80

def q(x, start, stop): return start <= x <= stop


coords = combinations(
    [10, 30, 50, 80],
    2
)

dlini = []

for start, stop in coords:
    flag = True

    for x in range(0, 100):
        if not (q(x, start, stop) <= (a(x) and (not p(x)))):
            flag = False
            break

    if flag:
        dlini.append(stop - start)

print(dlini)
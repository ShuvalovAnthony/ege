from itertools import combinations


def b(x):
    return 101 <= x <= 143


def c(x):
    return 144 <= x <= 199


def a(x, start, stop):
    return start < x < stop


coords = combinations(
    sorted([101, 143, 144, 199]), 2
)


dlini = []


for start, stop in coords:
    flag = True

    for x in range(0, 250):
        if not(
            a(x, start, stop) <=
            (b(x) or c(x))
        ):
            flag = False

    if flag:
        dlini.append(stop - start)


print(dlini)
print(max(dlini))
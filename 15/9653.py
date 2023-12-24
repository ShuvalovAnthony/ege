from itertools import combinations


def p(x):
    return 10 <= x <= 29


def q(x):
    return 13 <= x <= 18


# <= - наименьшая длина
# < - наибольшая
def a(x, start, stop):
    return start < x < stop


coords = combinations(
    sorted([10, 29, 13, 18]),
    2
)


# список, в котором я храню длины подошедших отрезков А
dlini = []


for start, stop in coords:
    flag = True

    for x in range(0, 30):
        if not (
            (
                a(x, start, stop) <=
                p(x)
            ) or
            q(x)
        ):
            flag = False
            break

    if flag:
        dlini.append(stop - start)



print(dlini)
print(max(dlini))

# from itertools import product

# def a(start, stop, x):
#     return start <= x <= stop


# dlini = set()

# for start, stop in product(range(-200, 200), range(-200, 200)):
#     flag = True

#     for x in range(-200, 200):
#         if not (
#             (a(start, stop, x) <= (x**2 <= 100)) and
#             ((x**2 <= 64) <= a(start, stop, x))
#         ):
#             flag = False
#             break

#     if flag:
#         dlini.add(stop - start)


# print(dlini, min(dlini))

dlini = set()

for start in range(-200, 200):
    for stop in range(-200, 200):
        flag = True

        for x in range(-200, 200):
            if not (
                ((start <= x <= stop) <= (x**2 <= 100)) and
                ((x**2 <= 64) <= (start <= x <= stop))
            ):
                flag = False
                break

        if flag:
            dlini.add(stop - start)


print(dlini, min(dlini))
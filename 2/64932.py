# print('_y__')

# for x in (0, 1):
#     for y in (0, 1):
#         for w in (0, 1):
#             for z in (0, 1):
#                 if (
#                     ((x == z) <= ((not y) or w)) !=
#                     ((w <= z) or (x <= y))
#                 ):
#                     print(x, y, w, z)


from itertools import *


def f(x, y, z, w):
    return ((x == z) <= ((not y) or w)) != ((w <= z) or (x <= y))


for a in product([0, 1], repeat=5): # 0, 1, 2, 3, 4
    t = [
        (a[0], 1, a[1], 0),
        (0, a[2], 1, a[3]),
        (0, a[4], 0 ,0)
    ]
    if len(t) == len(set(t)):
        for p in permutations('xywz'):
            if [f(**dict(zip(p, row))) for row in t] == [1, 1, 1]:
                print(''.join(p))
from itertools import permutations

data = [
    [0, 0, 0, 0, 1, 1, 1, 1], # 0
    [0, 0, 1, 1, 0, 0, 1, 1], # 1
    [0, 1, 0, 1, 0, 1, 0, 1], # 2
    [0, 1, 0, 1, 0, 0, 0, 1] # 3
]


def check(x, y, z, f):
    return ((not z) and x) or (x and y) == f

vars = {0: 'x', 1: 'y', 2:'z', 3:'f'}


for i in permutations(range(4), 4):
    x, y, z, f = i

    flag = True

    for i in range(8):
        if not check(
            data[x][i], data[y][i],
            data[z][i], data[f][i]
            ):
            flag = False
            break

    if flag:
        print(vars[x], vars[y], vars[z])

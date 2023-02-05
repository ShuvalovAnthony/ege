from itertools import permutations

# a1 = ['b', 'c', 'd'] разница между dict и list
# a2 = [1, 0, 1]
# print(list(zip(a1, a2)))
# print(dict(zip(a1, a2)))

def f(x, y, z):
    return (x<=y) and (y<=z)

t = [[1, 0, 0], [1, 0, 1]]

for p in permutations('xyz'):
    if [f(**dict(zip(p, r))) for r in t] == [0, 1]:
        print(p)
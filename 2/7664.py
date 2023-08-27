from itertools import *

# логическая функция пишется в return
# -> меняем на <= (импликация)
# ∨ -> or, ∧ -> and
def f(a, b, c, d):
    return ((a and b) == (not c)) and (b <= d)



t = [
    (1, 0, 0, 0),
    (1, 0, 1, 0),
    (1, 0, 1, 1),
    (1, 1, 0, 0)
]
if len(t) == len(set(t)):
    for p in permutations('abcd'):
        if [f(**dict(zip(p, r))) for r in t] == [1, 1, 1, 1]: # результат функции F сверху вниз
            print(''.join(p))
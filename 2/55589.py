from itertools import *

# логическая функция пишется в return
# -> меняем на <= (импликация)
# ∨ -> or, ∧ -> and
def f1(x, y, z, w):
    return (x <= y) == (w or (not z))

def f2(x, y, z, w):
    return (x <= y) and ((not w) == z)


for a in product([0, 1], repeat=5): #repeat = сколько пропусков в таблице
    # все строки как кортежи, по порядку православному
    # неизвестные поля - a[номер_по_порядку]
    t = [(a[0], 1, 0, 1), (a[1], 0, 0, 0), (0, a[2], 0, 0)] 
    if len(t) == len(set(t)):
        for p in permutations('xywz'):
            if (
                [f1(**dict(zip(p, r))) for r in t] == [a[3], 0, 0] and
                [f2(**dict(zip(p, r))) for r in t] == [0, a[4], 1]
            ): # результат функции F сверху вниз
                print(''.join(p))
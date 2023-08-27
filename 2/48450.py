from itertools import *

# логическая функция пишется в return
# -> меняем на <= (импликация)
# ∨ -> or, ∧ -> and
def f(x, y, z, w):
    return (w <= (y == z)) and (y == (z <= x))


for a in product([0, 1], repeat=2): #repeat = сколько пропусков в таблице
    # все строки как кортежи, по порядку православному
    # неизвестные поля - a[номер_по_порядку]
    t = [(a[0], 0, 0, 0), (0, a[1], 1, 1), (0, 0, 0, 1)] 
    if len(t) == len(set(t)):
        for p in permutations('xywz'):
            if [f(**dict(zip(p, r))) for r in t] == [1, 1, 0]: # результат функции F сверху вниз
                print(''.join(p))
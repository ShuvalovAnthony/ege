from itertools import *

# логическая функция пишется в return
# -> меняем на <= (импликация)
# ∨ -> or, ∧ -> and
def f(x, y, z, w):
    return (y and (x or z) or (not (y or z)) or w)


for a in product([0, 1], repeat=4): #repeat = сколько пропусков в таблице
    # все строки как кортежи, по порядку православному
    # неизвестные поля - a[номер_по_порядку]
    t = [
        (1, a[0], 0, 1),
        (a[1], 1, 0, a[2]),
        (0, 0, a[3], 1)
    ] 
    if len(t) == len(set(t)):
        for p in permutations('xywz'):
            if [f(**dict(zip(p, r))) for r in t] == [0, 0, 0]: # результат функции F сверху вниз
                print(''.join(p))
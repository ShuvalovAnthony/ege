from itertools import *

# логическая функция пишется в return
# -> меняем на <= (импликация)
# ∨ -> or, ∧ -> and
def f(x, y, z, w):
    return ((x <= y) == (y <= z)) and (y or w)


for a in product([0, 1], repeat=6): #repeat = сколько пропусков в таблице
    # все строки как кортежи, по порядку православному
    # неизвестные поля - a[номер_по_порядку]
    t = [
        (0, a[0], 0, a[1]),
        (0, 0, a[2], 0),
        (a[3], a[4], a[5], 0)
        ] 
    if len(t) == len(set(t)):
        for p in permutations('xywz'):
            if [f(**dict(zip(p, r))) for r in t] == [1, 1, 1]: # результат функции F сверху вниз
                print(''.join(p))



print('x', 'y', 'z', 'w')


for x in (0, 1):
    for y in (0, 1):
        for z in (0, 1):
            for w in (0, 1):
                if ((x <= y) == (y <= z)) and (y or w):
                    print(x, y, z, w)

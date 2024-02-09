from string import digits, ascii_lowercase
from itertools import product

alph = digits + ascii_lowercase


max_res = 0
answ = 0

for x, y in product(range(36), range(36)):
    try:
        res = (
            int('7' + alph[x] + '37' + alph[y], 14) +
            int('9' + alph[y] + '63', x) -
            int('15148', y)
        )
        
        if res > max_res:
            max_res = res
            answ = res//(x + y)

    except:
        ...


print(answ)
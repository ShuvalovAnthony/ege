from string import digits
from itertools import product

alph = digits[:8]


for x, y in product(alph, alph):
    res = int(x + '01' + y + '4', 9) +\
        int(x + y + '544', 8)

    if res%89 == 0:
        print(res//89)
        break
            
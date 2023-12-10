from string import digits, ascii_lowercase
from itertools import product


alph = digits + ascii_lowercase


for x, y, p in product(alph, alph, range(2, 37)):
    try:
        if (
            int('12', p)*int('34', p) ==
            int(x + y, p)**2
        ):
            print(int(y + x, p))
    except:
        ...

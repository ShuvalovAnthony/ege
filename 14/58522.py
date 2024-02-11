from string import digits, ascii_uppercase
from itertools import product

alph = digits + ascii_uppercase


for x, y, p in product(alph, alph, range(len(alph))):
    try:
        if (
            int("32", p)*int("14", p) == int(x + y + "2", x)
        ):
            print(int(y + x, p))
    except:
        ...
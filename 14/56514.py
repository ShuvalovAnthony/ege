from itertools import product
from string import digits, ascii_lowercase


alph = digits + ascii_lowercase


for x, y, p in product(alph, alph, range(len(alph))):
    try:
        if int('32' + x + '8', p) + int(x*3 + '9', p) == int(y*2 + '02', p):
            print(int(y*2 + x, p))
    except:
        ...
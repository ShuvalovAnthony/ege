from itertools import product
from string import digits, ascii_lowercase


alph = digits + ascii_lowercase


for x, y, z, p in product(alph, alph, alph, range(36)):
    try:
        if int(y + '4' + y, p) + int(y + '65', p) == int(x + z + '23', p):
            print(int(x + y + z, p))
    except:
        ...
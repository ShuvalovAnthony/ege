from string import digits, ascii_lowercase
from itertools import product


alph = digits + ascii_lowercase[:2]


for x, y in product(alph, alph):
    num1 = int(x + '231' + y, 12)
    num2 = int('78' + x + '98' + y, 14)
    res = num1 + num2
    if res%99 == 0:
        print(res//99)
        break


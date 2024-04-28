from itertools import product


def check(num: str):
    chetCount = 0
    for digit in num:
        chetCount += digit in "0246"
    
    return chetCount == 2


counter = 0
for num in product("0123456", repeat=7):
    num = ''.join(num)

    if (
        num[0] != '0' and
        check(num)
    ):
        counter += 1

print(counter)
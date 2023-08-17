from itertools import permutations
from string import digits


def to_num(digits: tuple):
    return int(''.join(digits))

def to_string(digits: tuple):
    return ''.join(digits)

def check(num):
    for i in range(len(num) - 1):
        if (int(num[i])%2 == 0 and int(num[i + 1])%2 == 0) or\
            (int(num[i])%2 == 1 and int(num[i + 1])%2 == 1): return False
    return True

counter = 0

for num in permutations(digits, 6):
    if num[0] != '0' and\
        to_num(num)%5 == 0 and\
        check(to_string(num)):
        counter += 1

print(counter)
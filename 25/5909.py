from string import digits
from itertools import product


def div(num):
    for i in range(2, int(num**0.5) + 1):
        if num%i == 0:
            if (num//i)%7 == 0: return num//i
            return False
    return False


def check(num):
    for i in range(10):
        if i%2: num = num.replace(str(i), '1')
        else: num = num.replace(str(i), '0')
    return ('00' not in num) and ('11' not in num)


limit = 5

for left in product(digits, repeat=6):
    left = ''.join(left)
    if check(left) and (left[0] != '0'):
        num = int(left + left[::-1][1:])
        if div(num) and limit: 
            limit -= 1            
            print(num, div(num))
        
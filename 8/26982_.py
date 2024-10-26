from string import digits
from itertools import product


def check(word):
    for i in range(10):
        if i%2 == 0:
            word = word.replace(str(i), "_")
        else:
            word = word.replace(str(i), "*")
    return not (('__' in word) or ('**' in word))

counter = 0

for num in product(digits, repeat=6):
    num = ''.join(num)
    if (
        (num[0] != "0") and
        (len(set(num)) == 6) and
        (num[-1] in '01') and
        check(num)
    ): 
        counter += 1

print(counter)
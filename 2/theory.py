from itertools import *


def f(x, y, z, w):
    return (x and y and not z) == (y or z or not w)


for a in product([0, 1], repeat=5):
    t = [(1, 1, a[0], 1), (a[1], 0, a[2], 0), (1, a[3], a[4], 1)]
    if len(t) == len(set(t)):
        for p in permutations('xywz'):
            if [f(**dict(zip(p, r))) for r in t] == [1, 1, 1]:
                print(''.join(p))








# from string import ascii_lowercase

# s = 'IUHFbjkdsfnsduigBHJKFBDSfnuisdkjfshuybYUGBHJFsdnfdsfbsdfuidsfa'.lower()


# letter_counter = {i: 0 for i in ascii_lowercase}

# for letter in s:
#     letter_counter[letter] += 1

# for _, value in letter_counter.items():
#     print(value)

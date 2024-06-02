from itertools import *

words = []

for word in product(sorted('АЕКПТЧ'), repeat=7):
    word = ''.join(word)
    words.append(word)


print(words.index("ПЕЧАТКА") - words.index("АПТЕЧКА") - 1)

from itertools import *

count = 0
flag = False

for word in product(sorted('АЕКПТЧ'), repeat=7):
    word = ''.join(word)

    if word == 'ПЕЧАТКА':
        flag = False

    if flag:
        count += 1

    if word == 'АПТЕЧКА':
        flag = True

print(count)
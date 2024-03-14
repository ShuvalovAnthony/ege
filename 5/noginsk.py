from itertools import product
from string import digits


for k in range(1, 8):
    res = set()
    for word in product(digits, repeat=k):
        word = "".join(word)
        if word[0] != '0':
            for i in word:
                res.add(int(word + i))

    l = len(res)
    print(k, len(res), l*9 + 9*10**k)
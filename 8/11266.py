from itertools import product

counter = 0

for word in product("ABCDEX", repeat=4):
    if word.count('X') == 1: counter += 1


print(counter)
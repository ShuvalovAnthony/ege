from itertools import product


counter = 0

for row in product((0, 1, 2, 3), repeat=3):
    if (row[0] + row[-1] > row[1] and\
        row[0] != 0):
        counter += 1


print(counter)
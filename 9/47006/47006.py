f = open("9/47006/47006.txt")

from itertools import permutations

rows = [
    [int(i) for i in row.split()] for row in f
]


def check_triangle(triplet):
    triplet = sorted(triplet)
    return triplet[-1] < triplet[0] + triplet[1]


def check_row(row):
    for triplet in permutations(row, 3):
        if not check_triangle(triplet): return False
    return True


counter = 0

for row in rows:
    counter += check_row(row)

print(counter)

    
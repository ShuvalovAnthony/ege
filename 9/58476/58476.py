f = open("9/58476/58476.txt")

nums = [[int(i) for i in row.split()] for row in f]


def check(row):
    row = sorted(row)

    if (
        (row[-1] == row[-2]) or
        (len(set(row)) == len(row))
    ): return False

    return row[-1] > sum(row[:-1])/5*3


counter = 0

for row in nums:
    counter += check(row)
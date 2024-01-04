f = open('9/58517/58517.txt')


nums = [
    [int(i) for i in row.split()] for 
    row in f
]


def check(row):
    row = sorted(row)
    if (
        (row[0] != row[1]) and
        (len(set(row)) != len(row)) and
        (row[-1] > sum(row[:-1])/5*3)
    ): return True

    return False


counter = 0

for row in nums:
    counter += check(row)

print(counter)

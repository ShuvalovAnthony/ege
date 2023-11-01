f = open('9/4614/4614.txt')

data = [[int(i) for i in row.split()] for row in f]


def check(row):
    row = sorted(row)
    if (
        len(set(row)) == 3 and
        row[-1] < sum(row[:-1])
    ): return True
    return False


counter = 0

for row in data:
    counter += check(row)

print(counter)
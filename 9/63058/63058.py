f = open('9/63058/63058.txt')

data = [[int(i) for i in row.split()] for row in f]


def check(row):
    if len(set(row)) == len(row): return False
    row = sorted(row)

    summa_povtor = 0
    for num in row:
        if row.count(num) > 1:
            summa_povtor += num

    if (
        (row[-1] != row[-2]) and
        (summa_povtor < row[-1])
    ): return True
    return False


kolichestvo = 0

for row in data:
    if check(row):
        kolichestvo += 1

print(kolichestvo)
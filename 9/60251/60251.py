f = open('9/60251/60251.txt')

data = [[int(i) for i in row.split()] for row in f]


def check(row):
    if len(set(row)) != 5: return False

    summa_povtor = 0
    for num in row:
        if row.count(num) == 2: summa_povtor += num
        if row.count(num) == 3: return False
    return summa_povtor/4 < sum(row)/7

counter = 0

for row in data: counter += check(row)

print(counter)
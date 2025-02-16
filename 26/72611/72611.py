f = open("ege/26/72611/26.txt")

data = []


for row in f:
    row = [int(i) for i in row.split()]
    id = row[0]
    row = row[1:]
    summa = sum([i for i in row])
    pluses = sum([i for i in row if i > 0])
    answ = len([i for i in row if i != 0])
    data.append([id, summa, pluses, answ])

data = sorted(data, key=lambda x: (-x[1], -x[2], -x[3], x[0]))


passed = data[:len(data)//4]
unpassed = data[len(data)//4:]


for row in unpassed:
    if (
        row[1:] == passed[-1][1:]
    ):
        passed.append(row)
        unpassed = unpassed[1:]


counter = 0
for row in passed:
    counter += row[1:] == passed[1699][1:]

print(unpassed[0][0], counter)
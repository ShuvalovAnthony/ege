f = open("ege/26/72584/26.txt")


data = []

for row in f:
    row = [int(i) for i in row.split()]
    id = row[0]
    row = row[1:]
    summa = sum(row)
    pluses = sum([i for i in row if i > 0])
    answs = len([i for i in row if i != 0])
    data.append([id, summa, pluses, answs])


# x[0]     x[1] - summa     x[2] - pluses   x[3] - answe
data = sorted(data, key=lambda x: (
    -x[1],
    -x[2],
    -x[3],
    x[0]
))


passed = data[:len(data)//3]
unpassed = data[len(data)//3:]


for row in unpassed:
    if row[1:] == passed[-1][1:]:
        passed.append(row)
        unpassed = unpassed[1:]


counter = 0
for row in passed:
    counter += row[1:] == passed[1499][1:]


print(unpassed[0][0], counter)
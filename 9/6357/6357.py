f = open('9/6357/6357.txt')

data = [list(map(int, i.split())) for i in f]

def check(row):
    povtor = []
    nepovtor = []
    for num in row:
        if row.count(num) >= 2: povtor.append(num)
        else: nepovtor.append(num)

    return (
        bool(povtor and nepovtor) and
        sum(nepovtor)/len(nepovtor) < sum(povtor)/len(povtor)
    )


counter = 0

for row in data: counter += check(row)

print(counter)

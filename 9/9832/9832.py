f = open('9/9832/9832.txt')

data = [list(map(int, i.split())) for i in f]

def check(row):
    if (
        len(set(row)) != 5 or
        row.count(max(row)) == 2
    ): return False

    for num in row:
        if row.count(num) == 3: return False

    return sum(row)

for row in data:
    if check(row):
        print(check(row))
        break
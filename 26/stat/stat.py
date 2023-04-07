from array import array

f = open('26/stat/stat.txt')

n = int(f.readline())

rows = {}

for i in f:
    row, col = map(int, i.split())
    try: rows[row].add(col)
    except:rows[row] = {col,}

rows = dict(sorted(rows.items()))

def find_max_line(row: list) -> int:
    row = sorted(row)
    print(row)


find_max_line(rows[1])
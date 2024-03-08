f = open("26/55643/26.txt")

rows = {i: [] for i in range(10**5 + 1)}

for row in f:
    i, coord = map(int, row.split())
    rows[i].append(coord)


def check_row(row):
    if not row: return False
    row = sorted(row)
    start = row[0]
    max_len = 0
    for i in range(len(row) - 1):
        if row[i + 1] - row[i] <= 9:
            continue
        else:
            max_len = max(row[i] - start + 1, max_len)
            start = row[i + 1]

    return max_len


good_rows = []

for key, row in rows.items():
    if check_row(row):
        good_rows.append([check_row(row), key])

good_rows = sorted(good_rows)

print(good_rows[-5:]) # взять ласт
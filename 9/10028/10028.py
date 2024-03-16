f = open("9/10028/9_10028.txt")

data = [
    [int(i) for i in row.split()] for row in f
]


def check_row(row):
    row = sorted(row)
    return (
        (len(set(row)) != len(row)) +
        (row[0]*row[-1] <= row[1] + row[2]) +
        (row[0] + row[-1] == row[1] + row[2])
    ) == 1


summ = 0

for i in range(len(data)):
    if check_row(data[i]):
        summ += i + 1

print(summ)
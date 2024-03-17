f = open("9/09876/1.txt")

marks = [
    [int(i) for i in row.split()] for row in f
]


def check(row):
    row = sorted(row)[1:-1]
    return sum(row)/len(row) >= 8


counter = 0

for row in marks:
    counter += check(row)

print(counter)
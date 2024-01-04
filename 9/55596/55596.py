f = open('9/55596/55596.txt')


nums_by_rows = [
    [int(i) for i in row.split()] for
    row in f
]

all_nums = []
for row in nums_by_rows:
    all_nums += row


def check(row):
    for cell in row:
        if (
            (row.count(cell) == 1) and
            (all_nums.count(cell) == 46)
        ):
            return True
    return False


counter = 0

for row in nums_by_rows:
    counter += check(row)

print(counter)

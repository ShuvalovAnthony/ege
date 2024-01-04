f = open('9/59714/59714.txt')

nums = [
    [int(i) for i in row.split()] for row in f
]


def check(row):
    povtor = []
    nepovtor = set()

    for num in row:
        if row.count(num) == 2:
            povtor.append(num)
        elif row.count(num) == 1:
            nepovtor.add(num)

    if (
        (
            (len(povtor) == 4) and
            (len(nepovtor) == 3)
        ) and
        (
            sum(nepovtor)/3 > sum(povtor)/4
        )
    ): return True

    return False




counter = 0

for row in nums:
    counter += check(row)

print(counter)
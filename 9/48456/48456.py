f = open('9/48456/48456.txt')

nums = [
    [int(i) for i in row.split()] for row in f
]

def check(row):
    povtor = set()
    nepovtor = []
    for num in row:
        if row.count(num) == 1:
            nepovtor.append(num)
        elif row.count(num) == 2:
            povtor.add(num)
        else:
            return False

    if (
        (
            len(set(row)) == 4
        ) and
        (
            (sum(povtor)) > (sum(nepovtor))
        )
    ): return True
    return False

kolichestvo = 0

for row in nums:
    if check(row):
        kolichestvo += 1



print(kolichestvo)
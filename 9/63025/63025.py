f = open('9/63025/63025.txt')


nums = [
    [int(i) for i in row.split()] for row in f
]


def check(row):
    row = sorted(row)
    summa_povtor = 0

    for i in row:
        if row.count(i) > 1:
            summa_povtor += i
    
    if (
        (len(set(row)) != len(row)) and
        (row[-1] != row[-2]) and
        (summa_povtor > row[-1])
    ): return True

    return False



counter = 0

for row in nums:
    counter += check(row)

print(counter)
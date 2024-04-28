f = open("9/12241/12241.txt")

nums = [
    [int(i) for i in row.split()] for row in f
]


def check(row: list):
    povtor = []
    nepovtor = []

    for num in row:
        if row.count(num) > 2: return False

        if row.count(num) == 2: povtor.append(num)
        else: nepovtor.append(num)
    
    return (
        (len(povtor) == 6) and
        (
            (min(povtor) + max(povtor))/2 < sum(nepovtor)
        )
    )

counter = 0
for row in nums:
    # if check(row):
    #     counter += 1
    counter += check(row)

print(counter)
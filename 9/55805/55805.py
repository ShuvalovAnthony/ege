f = open('9/55805/55805.txt')


nums = [
    [int(i) for i in row.split()] for row in f
]


def check(row): # row = [5, 3, 1, 4, 2]
    if len(set(row)) != len(row): 
        return False

    row = sorted(row) # row = [1, 2, 3, 4, 5]

    if (
        3*(row[-1] + row[0]) <= 2*(row[1] + row[2] + row[3])
    ): return True
    else:
        return False
    

counter = 0

for row in nums:
    print(row)
    # if check(row):
    #     counter += 1
    counter += check(row)


print(counter)
f = open("9/59779/59779.txt")


nums = [
    [int(i) for i in row.split()] for row in f
]



def check(row):
    flag = False
    povtor = 0
    summaNepovtor = 0
    for num in row:
        if row.count(num) == 4:
            flag = True
            povtor = num
        else:
            summaNepovtor += num

    if (
        ((len(set(row)) == 4) and flag) and
        (povtor > summaNepovtor/3)
        ): return True
    
    return False


counter = 0

for row in nums:
    counter += check(row)

print(counter)
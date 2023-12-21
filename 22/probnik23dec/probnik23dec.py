f = open("22/probnik23dec/data.txt")

data = [[int(i) for i in row.split()] for row in f]


for i in range(25):
    tmp_counter = 0
    for stop, start in data:
        if start <= i <= stop:
            tmp_counter += 1
    print(i, tmp_counter)
    
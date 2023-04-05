f = open('26/stat/stat.txt')

n = int(f.readline())

coords = tuple(tuple(map(int, i.split())) for i in f)



for row_num in range(1, 10**5 + 1):
    tmp_row = [0]*10**5
    for i in coords:
        row, col = i[0], i[1]
        if row == row_num:
            tmp_row[col] = 1
    print(tmp_row.count(1), )
    
        
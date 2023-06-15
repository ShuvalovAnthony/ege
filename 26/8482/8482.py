f = open('26/8482/26_8482.txt')

n = int(f.readline())
k = int(f.readline())


times = sorted(
    [
        [int(i) for i in j.split()] for j in f
    ]
)


tables = [-1]*k # времена освобождения
counter = 0


for start, stop in times:
    flag = True
    min_delta = 11
    temp_table_num = -1
    for table_num in range(k):
        if start >= tables[table_num] and flag:
            tables[table_num] = stop + 7
            counter += 1
            last_table = table_num
            flag = False
            break
    
    if flag:
        for table_num in range(k):
            if start + 10 >= tables[table_num]:
                if abs(start - tables[table_num]) < min_delta:
                    temp_table_num = table_num
                    min_delta = abs(start - tables[table_num])
                    break
    
    tmp_stop  = stop + min_delta + 7

    if (temp_table_num != -1 )and (tmp_stop <= 23*60):
        print(min_delta)
        tables[temp_table_num] = tmp_stop
        counter += 1
        last_table = temp_table_num
    
    
print(counter, last_table + 1)
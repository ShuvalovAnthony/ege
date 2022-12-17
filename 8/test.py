# Сколько 4х буквеных слов из букв АОЖДКИ начинается с гласной и заканчивается на Ж или Д
count = 0
for a1 in 'АОЖДКИ':
    for a2 in 'АОЖДКИ':
        for a3 in 'АОЖДКИ':
            for a4 in 'АОЖДКИ':
                res = a1 + a2 + a3 + a4
                if (res[0] in 'АОИ') and (res[-1] in 'ЖД'):
                    print(res)
                    count += 1
    
print(count)
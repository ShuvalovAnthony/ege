def check(num):
    summa_nechet = 0
    for i in str(num):
        if int(i)%2: summa_nechet += int(i)
    return num%summa_nechet == 0

all_variants = [''] + [str(i).zfill(2) for i in range(10)]  + [str(i) for i in range(100)]


for first_star in all_variants:
    for second_star in all_variants:
        res = int('124' + first_star + '5' + second_star + '79')
        if check(res) and res <= 10**8:
            print(res, sum(map(int, list(str(res)))))

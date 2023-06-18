from operator import le


f = open('1_types of data/ege/27/37162/27_B.txt')

n = int(f.readline())

nums = []

for i in f:
    nums.append(int(i))



answ_summa = 0
answ_len = 0

for i in range(n):
    summa = 0
    len_summa = 0
    for j in range(i, n):
        summa += nums[j]
        len_summa += 1
        if (summa%89 == 0) and (summa > answ_summa):
            answ_summa = summa
            answ_len = len_summa
    if i%100 == 0: print(i)


print(answ_summa, answ_len)

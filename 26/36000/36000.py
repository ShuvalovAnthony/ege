f = open('26/36000/36000.txt')


chet_nums = []
nechet_nums = []


for i in f:
    num = int(i)
    if num%2 == 0:
        chet_nums.append(num)
    else:
        nechet_nums.append(num)


all_nums = set(chet_nums + nechet_nums)

counter = 0
max_summa = 0

for chet_num in chet_nums:
    for nechet_num in nechet_nums:
        summa = chet_num + nechet_num
        if summa in all_nums:
            counter += 1
            max_summa = max(max_summa, summa)


print(counter, max_summa)

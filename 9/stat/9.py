f = open('9/stat/data.txt')



nums_postrochno = [tuple(map(int, i.split())) for i in f]
all_nums = []
for stroka in nums_postrochno: all_nums += stroka



counter = 0

for stroka in nums_postrochno:
    for num in stroka:
        if (
            stroka.count(num) == 1 and
            all_nums.count(num) == 46
        ): counter += 1


print(counter)
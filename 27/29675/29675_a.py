f = open('ege/27__/29675/inf_22_10_20_27a.txt')


n = f.readline()


nums = []

diffs = [] # 1 2 3 4 5


for i in f:
    a, b = map(int, i.split())
    nums.append(sorted([a, b]))

summa = 0

for i in nums:
    diffs.append(i[1] - i[0])
    summa += max(i)


if summa%3 == 0:
    print(summa)
else:
    for i in sorted(diffs):
        if (summa - i)%3 == 0:
            print(summa - i)



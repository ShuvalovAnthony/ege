f = open('27/27989/27989_B.txt')

nums = [int(i) for i in f]


krat_26 = 0
krat_13 = 0
krat_2 = 0
not_krat = 0

for i in nums:
    if i%26 == 0:
        krat_26 += 1
    elif i%13 == 0:
        krat_13 += 1
    elif i%2 == 0:
        krat_2 += 1
    else:
        not_krat += 1

res = krat_26*not_krat + \
    krat_13*krat_2 + \
    krat_26*krat_2 + \
    krat_26*krat_13 + \
    krat_26*(krat_26 - 1)//2


print(res)
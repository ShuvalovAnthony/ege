counter = 0

def krat_2(num):
    return num%2 == 0

def krat_3(num):
    return num%3 == 0

def check(num:list):
    if (
        krat_2(num[0]) and krat_2(num[2]) and krat_2(num[4]) and\
        krat_3(num[1]) and krat_3(num[3])
    ) or\
    (
        krat_3(num[0]) and krat_3(num[2]) and krat_3(num[4]) and\
        krat_2(num[1]) and krat_2(num[3])
    ):
        return True
    return False


for i in range(1, 10**6):
    num = []
    start = i
    while start > 0:
        num.append(start%15)
        start //= 15
    if len(num) == 5:
        counter += check(num)


print(counter)

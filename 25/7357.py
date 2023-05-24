def chek(num):
    num = str(num)
    if (
        num[0] in '2468' and
        num[1:4] == '136'
    ):
        return True 


max_chislo = 0
counter = 5
for num in range(53191, 10**10 + 1, 53191):
    if chek(num):
        print(num, num//53191, 10**10 - num)
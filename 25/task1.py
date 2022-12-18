# ищем первое число кратное 3123 на промежутке 0 -> 10**9


# 1 000 000 000

# 999 999 999

# 12 * 63 ? 5 ? -> * - это либо 0 либо 1 либо 2 символа



# ''
# '0' -> '99'

stars = [''] + [str(i) for i in range(100)]


min_num = 0

flag = False
for star in stars:
    if flag:
        break
    for qs1 in '0123456789':
        for qs2 in '0123456789':
            num = int('12' + star + '63' + qs1 + '5' + qs2)
            if num%3123 == 0:
                min_num = num
                flag = True


def check_mask(num):
    num = str(num)
    if (num[:2] == '12') and \
        (num[-2] == '5') and\
        (num[-5:-3] == '63'):
        return True
    return False


for i in range(min_num, 10**9 + 1, 3123):
    if check_mask(i):
        print(i)   

# 12363957
# 120663351
# 120963159
# 124763850
# 125063658
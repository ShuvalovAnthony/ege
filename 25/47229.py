def mask(num):
    num = str(num)
    if num[0] == '1' and num[2:6] == '2139' and \
        num[-1] == '4':
        return True
    return False



for i in range(2023, 10**10, 2023):
    if mask(i): print(i, i//2023)


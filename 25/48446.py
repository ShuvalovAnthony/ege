def check(num):
    num = str(num)
    if (
        num[0] == '1' and
        num[2:5] == '493' and
        num[-2::] == '41'
    ): return True
    return False




for num in range(2023, 10**10 + 1, 2023):
    if check(num): print(num)
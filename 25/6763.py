def mask(num):
    num = str(num)
    if (
        num[:4] == '6323' and
        num[-4:-1] == '353'
    ): return True
    return False



for i in range(28, 10**9, 28):
    if mask(i):
        print(i, i//28)
def check(n: int):
    n = str(n)
    if n[0] == '1' and \
        n[2:6] == '2139' and \
        n[-1] == '4':
        return True
    return False



for i in range(2023, 10**10 + 1, 2023):
    if check(i): print(i, i//2023)


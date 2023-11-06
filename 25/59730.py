def mask(n: int):
    n = str(n)

    # 3?1*57
    if (
        n[0] == '3' and
        n[2] == '1' and
        n[-2:] == '57'
    ): return True
    return False


for n in range(2023, 10**8 + 1, 2023):
    if mask(n):
        print(n, n//2023)
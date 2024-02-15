def check(num): # 16 -> 2 ..... 15
    delit = set()
    for i in range(2, int(num**0.5) + 1):
        if num%i == 0:
            delit.add(i)
            delit.add(num//i)

    if len(delit) == 2: return delit
    return False



for num in range(174457, 174505 + 1):
    if check(num):
        print(*sorted(list(check(num))))
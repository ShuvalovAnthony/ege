def summa_cifr(num):
    return sum([int(i) for i in str(num)])

def simple(n):
    for i in range(2, int(n**0.5) + 1):
        if n%i == 0: return False
    return True

def mask(num, mask_right_part):
    num = str(num)
    if num[:4] != '1234': return False
    if num[4:] != str(mask_right_part): return False
    return True

answ = {}

for i in range(1, 7):
    for num in range(1234*10**i, 1235*10**i):
        p = summa_cifr(int(str(num)[4:]))
        if simple(p) and\
            num%((p + 2)**3) == 0 and\
            p:
            try: answ[p]
            except: answ[p] = num


for i in answ:
    print(answ[i], i)
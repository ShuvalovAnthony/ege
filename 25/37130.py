# sposob 1

def not_trivial_delit(n:int):
    deliteli = []
    for i in range(2, int(n**0.5) + 1):
        if n%i == 0:
            deliteli += [i, n//i]
    for i in sorted(deliteli):
        if str(i)[-1] == '7' and i != 7:
            return i
    return False

counter = 5

for i in range(6*10**5 + 1, 10**12):
    if not_trivial_delit(i):
        print(i, not_trivial_delit(i))
        counter -= 1
    if not counter: break
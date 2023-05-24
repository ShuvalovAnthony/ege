def not_trivial_delit(n:int):
    deliteli = []
    for i in range(2, int(n**0.5) + 1):
        if n%i == 0:
            deliteli += [i, n//i]
    return sorted(set(deliteli))


counter = 5

for i in range(452021 + 1, 10**12):
    deliteli = not_trivial_delit(i)
    if deliteli:
        m = deliteli[0] + deliteli[-1]
        if m%7 == 3:
            print(i, m)
            counter -= 1
    if counter == 0:
        break

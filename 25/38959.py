def delit(num):
    deliteli = set()
    for i in range(1, int(num**0.5) + 1):
        if num%i == 0:
            deliteli.add(i)
            deliteli.add(num//i)
    
    return deliteli


def check(num):
    deliteli = sorted(list(delit(num)))
    if len(deliteli) < 6: return False

    proizved = 1
    for i in range(1, 6):
        proizved *= deliteli[i]
    return proizved



counter = 0

for num in range(2*10**8 + 1, 2*10**9):
    res = check(num)
    if 0 < res < num:
        counter += 1
        print(res)
    
    if counter == 5: break


def delit(n: int):
    deliteli = []
    for i in range(2, n + 1, 2):
        if n%i == 0:
            deliteli.append(i)
        if len(deliteli) > 6:
            return False
    if len(deliteli) == 6:
        return deliteli
    return False


for i in range(95632, 95700 + 1):
    if delit(i): 
        print(delit(i))
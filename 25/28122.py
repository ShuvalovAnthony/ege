def delit(n):
    if n**0.5 == int(n**0.5): # отбрасываем числа, из которых
        return False    # можно извлечь кв корень

    # тривиальные делители - уже дают 2 делителя - 1 и n
    # нам нужно 2 нетривиальных делителя (в сумме - 4)
    deliteli = []
    for i in range(2, int(n**0.5) + 1):
        if n%i == 0:
            deliteli += [i, n//i]
        if len(deliteli) > 2: return False
    if len(deliteli) == 2: return deliteli
    return False


for i in range(489421, 489440 + 1):
    if delit(i): print(1, *delit(i), i)
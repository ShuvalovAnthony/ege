def delit(num: int):
    deliteli = [] # список куда записываются делители

    for i in range(2, num): # перебираем все числа, кроме 1 и самого числа n
        if num%i == 0: # если n кратно числам из перебора...
            deliteli.append(i)  #  - записываем его в список делителей
            if len(deliteli) > 2: # как только делителей больше чем надо... 
                return False    # прерываем цикл и возвращаем False
    # 0, 1, 2
    if len(deliteli) == 2: # если делителей 2 - возвращаем их списком
        return deliteli

    return False   # если 0 или 1 (ост варианты) - тоже False


for i in range(174457, 174506):
    if delit(i):
        print(*delit(i))

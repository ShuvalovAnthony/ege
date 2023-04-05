def check(num):
    deliteli = []
    for delitel in range(1, num + 1, 2): # от 2 до числа не включительно
        if num%delitel == 0: # если число делится на делитель
            deliteli.append(delitel)
    if len(deliteli) == 6:
        return deliteli
    return False


for num in range(95632, 95650 + 1):
    if check(num): print(check(num))
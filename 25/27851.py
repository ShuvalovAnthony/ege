def check(num):
    deliteli = []
    for delitel in range(2, num): # от 2 до числа не включительно
        if num%delitel == 0: # если число делится на делитель
            deliteli.append(delitel)
    if len(deliteli) == 4:
        return deliteli
    return False


for num in range(210235, 210300 + 1):
    if check(num): print(check(num))
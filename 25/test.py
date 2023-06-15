def deliteli(num):
    counter = 0
    for i in range(1, int(num**0.5) + 1):
        if num%i == 0:
            counter += 2
    return counter


print(deliteli(19905392888))
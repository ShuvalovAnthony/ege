# n = 1 2 3...

# bin(n)[2:]

# r = int(n, 2)


for n in range(1, 1000):
    n_bin = bin(n)[2:] # двоичная запись n, str
    
    # дописываем остаток от деления суммы цифр на 2 ДВАЖДЫ
    # для 2ого числа сумма цифр - колво единиц
    for i in range(2):
        n_bin += str(n_bin.count('1')%2)

    # перевод в 10ую из 2ой
    r = int(n_bin, 2)

    if r > 97:
        print(n)
        break
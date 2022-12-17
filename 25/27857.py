def delit(n):
    count = 0 # счетчик делителей (сами делители в задаче не нужны)

    for i in range(1, n + 1): # все делители от 1 до самого числа вкл
        if n%i == 0:
            count += 1

    return count, n

max_count = 0
chislo = 0


for i in range(84052, 84131):
    if delit(i)[0] > max_count: # как вчера в задачке с модой - 2 варианта
        max_count = delit(i)[0]
        chislo = delit(i)[1] # меняем макс число
        

print(max_count, chislo)
result = set()

for n in range(100, 3000 + 1):
    n_bin = bin(n)[3:]
    
    if n_bin.count('1') == 0: # Если нет 1 - избегаем ошибки
        r = 0
    else:
        r = int(n_bin, 2)

    result.add(n - r)


print(result, len(result))
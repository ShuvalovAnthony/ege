for num in range(1, 1000): # на вход подается число
    num_bin = bin(num)[2::] # строится его довичная запись
    # проверяется кратность трем
    if num%3 == 0: # если кратно то...
        num_bin += num_bin[-3::] # добавляем младшие 3 разряда
    else: # иначе (не кратно 3)
        num_bin += bin(3 * (num%3))[2::] # добавляем двоичную запись
                    # числа 3 умнож на остаток от деления num на 3
    res = int(num_bin, 2) # переводим в 10ную систему
    if res < 100:  # если <100 - печатаем
        print(num)
        
for a in range(1000):
    flag = True # мы говорим, что этот А - правильный
    for x in range(1, 1000):
        if not ( # если хотя бы 1 раз х не даст выполнения условия из задания
            (x&33 == 0) <= ((x&45 != 0) <= (x&a != 0))
        ):
            flag = False # тогда мы бракуем А
            break # и перестаем искать х
    
    if flag: # если мы прошли по всем х и флаг не забраковался
        print(a) # значит, это искомый А
        break # дальше не ищем тк нужен минимальный
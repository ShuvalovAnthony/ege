combos = [] # список рядом стоящих гласных и согласных

for a1 in 'АО':
    for a2 in 'АО':
        combos.append(a1 + a2)
# print(combos) 

for a1 in 'ПРБЛ':
    for a2 in 'ПРБЛ':
        combos.append(a1 + a2)
# print(combos)

count = 0

for a1 in 'ПАРБОЛ': # ПАРАБОЛА
    for a2 in 'ПАРБОЛ':
        for a3 in 'ПАРБОЛ':
            for a4 in 'ПАРБОЛ':
                for a5 in 'ПАРБОЛ':
                    for a6 in 'ПАРБОЛ':
                        for a7 in 'ПАРБОЛ':
                            for a8 in 'ПАРБОЛ':
                                res = a1 + a2 + a3 + a4 + a5 + a6 + a7 + a8
                                if ((res.count('П') == 1) and (res.count('А') == 3) and (res.count('Р') == 1) and
                                (res.count('Б') == 1) and (res.count('О') == 1) and (res.count('Л') == 1)):
                                    # ниже отсекаем слова где глас/согл попарно подряд
                                    flag = True # по умолчанию слово ок
                                    for combo in combos: # бежим по всем запретным комбинациям
                                        if combo in res: # если запретная комбо есть в слово - меняем флаг на фолс
                                            flag = False
                                            break # дальше не проверяем, тк достаточно 1 запретной комбо
                                                    # чтобы забраковать слово
                                    if flag: # if flag ----> if flag == True - соотв если слово не забраковано оно ок
                                        count += 1 # увеличиваем колво ок слов

                                    
print(count)
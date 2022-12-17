combos = []

for g1 in 'ао':
    for g2 in 'ао':
        combos.append (g1 + g2)

for g1 in 'мрхс':
    for g2 in 'мрхс':
        combos.append (g1 + g2)
    
counter =  0
for g1 in 'росмах':
    for g2 in 'росмах':
        for g3 in 'росмах':
            for g4 in 'росмах':
                for g5 in 'росмах':
                    for g6 in 'росмах':
                        for g7 in 'росмах':
                            for g8 in 'росмах':
                                res = g1 + g2 + g3 + g4 + g5 + g6 + g7 + g8
                                if ((res.count('р') == 1) and (res.count('о') == 2) and (res.count('с') == 1) and\
                                    (res.count('м') == 1) and (res.count('а') == 2) and (res.count('х') == 1)):
                                    flag = True 
                                    for combo in combos:
                                        if combo in res:
                                            flag = False
                                            break
                                    if flag:
                                        counter += 1

print(counter)
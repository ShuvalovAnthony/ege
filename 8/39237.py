index = 0

for a1 in 'АВОРТ':
    for a2 in 'АВОРТ':
        for a3 in 'АВОРТ':
            for a4 in 'АВОРТ':
                res = a1 + a2 + a3 + a4
                index += 1
                if res == 'ТАРА':
                    print(index)

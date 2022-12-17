index = 0


for a1 in 'АБРТЫ':
    for a2 in 'АБРТЫ':
        for a3 in 'АБРТЫ':
            for a4 in 'АБРТЫ':
                for a5 in 'АБРТЫ':
                    res = a1 + a2 + a3 + a4 + a5
                    index += 1
                    

                    if ('Ы' not in res):
                        x = res.replace('АА', '')
                        if res == x:
                            print(index, res)
                        




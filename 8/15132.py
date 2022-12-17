index = 0

for a1 in 'ПАРУС':
    for a2 in 'ПАРУС':
        for a3 in 'ПАРУС':
            for a4 in 'ПАРУС':
                res = a1 + a2 + a3 + a4
                index += 1
                print(index, res)
                if res[0] == 'У':
                    print(index, '---------------------------------')
                    break

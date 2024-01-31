alph = sorted('АЛГОРИТМ')

counter = 0

for a1 in alph:
    for a2 in alph:
        for a3 in alph:
            for a4 in alph:
                word = a1 + a2 + a3 + a4
                counter += 1
                if word[0] == 'Г' and word[1] == 'О':
                    print(counter)
                    
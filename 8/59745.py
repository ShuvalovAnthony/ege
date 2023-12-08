index = 1
kollichestvo = 0
for a1 in (sorted('алгоритм')):
    for a2 in (sorted('алгоритм')):
        for a3 in (sorted('алгоритм')):
            for a4 in (sorted('алгоритм')):
                for a5 in (sorted('алгоритм')):
                    word = a1+a2+a3+a4+a5

                    if (
                        (a1 != 'г')and
                        (index%2!=0) and
                        (word.count('и')>=2)
                    ):
                        kollichestvo += 1
                        print(word)

                    index +=1

print(kollichestvo)
count = 0
for a1 in 'ЕГЭ':
    for a2 in 'ЕГЭ':
        for a3 in 'ЕГЭ':
            for a4 in 'ЕГЭ':
                for a5 in 'ЕГЭ':
                    res = a1 + a2 + a3 + a4 + a5
                    if res[0] in 'ЕЭ':
                        count += 1
print(count)
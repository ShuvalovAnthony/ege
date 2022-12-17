counter = 0

for a1 in '1234':
    for a2 in '1234':
        for a3 in '1234':
            for a4 in '1234':
                for a5 in '1234':
                    res = a1 + a2 + a3 + a4 + a5
                    if (res.count('1') == 2):
                        counter += 1


print(counter)
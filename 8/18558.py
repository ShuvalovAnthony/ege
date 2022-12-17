counter = 0

for a1 in 'иван':
    for a2 in 'иван':
        for a3 in 'иван':
            for a4 in 'иван':
                for a5 in 'иван':
                    res = a1 + a2 + a3 + a4 + a5
                    # if res.count('и') >= 1:
                    # if res.count('и') != 0:
                    if 'и' in res:
                        counter += 1

print(counter)
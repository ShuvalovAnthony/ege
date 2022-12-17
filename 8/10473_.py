count = 0
for n1 in '1234':
    for n2 in '1234':
        for n3 in '1234':
            for n4 in '1234':
                for n5 in '1234':
                    res = n1 + n2 + n3 + n4 + n5
                    if res.count('1') == 2:
                        count += 1
print(count)
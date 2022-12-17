count = 0

for a1 in '12345':
    for a2 in '12345':
        for a3 in '12345':
            for a4 in '12345':
                for a5 in '12345':
                    res = a1 + a2 + a3 + a4 + a5
                    
                    if res.count('1') == 3:
                        print(res)
                        count += 1

print(count)
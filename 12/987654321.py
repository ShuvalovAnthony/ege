# yandex

for n in range(4, 500):
    s = '8' + '5'*n

    while ('8858' in s) or ('555' in s):
        if '8858' in s:
            s = s.replace('8858', '4', 1)
        else:
            s = s.replace('555', '58', 1)
        
        if '5858' in s:
            s = s.replace('5858', '85', 1)

    
    count = 0
    for i in s: count += int(i)

    if count == 66:
        print(n)
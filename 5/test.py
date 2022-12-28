for n in range(100, 300):
    start_n = n
    n = bin(n)[2:]


    for i in range(3):
        if n.count('0') == n.count('1'):
            n += n[-1]
        else:
            if n.count('0') < n.count('1'):
                n += '0'
            else:
                n += '1'

    r = int(n, 2)
    if r%4 == 0:
        print(start_n, r)    

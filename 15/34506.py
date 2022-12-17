for a in range(0, 100):
    flag = True
    for x in range(0, 100):
        if ((not (x & 25 != 0)) or ((not (x & 17 == 0)) or (x & a != 0))) == False:
            flag = False
            break
    if flag: print(a)

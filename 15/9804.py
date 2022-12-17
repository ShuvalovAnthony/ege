# x & 29 ≠ 0 → (x & 17 = 0 → x & А ≠ 0)




for a in range(0, 100): # a = 0
    flag = True
    for x in range(0, 100): # x = 0 .... 10000
        if ((x & 29 == 0) or ((x & 17 != 0) or (x & a != 0))) == False:
            flag = False
            break
    if flag:
        print(a)
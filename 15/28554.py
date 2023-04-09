for a in range(1, 1000):
    flag = True 
    for x in range(1000):
        for y in range(1000):
            if ((x * y < 140) or (y > a) or (x > a)) ==  False:
                flag = False 
                break
    if flag:
        print(a)
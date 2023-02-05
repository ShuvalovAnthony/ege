for a in range(1000): # a = 15
    flag = True

    for x in range(1000): # a = 15 x= 0, 1, 2, 3......
        if not ((x&17 == 0) <= ((x&29 != 0) <= (x&a != 0))):
            flag = False
            break
    
    if flag: # (if flag <======> if flag == True)
        print(a)
        break
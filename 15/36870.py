for a in range(1000):
    flag = True # это значит что мы предполагаем что это А
            # нам подходит
    for x in range(1000):
        if not ((x&49 == 0) <= ((x&28 != 0) <= (x&a != 0))):
            flag = False
            break
    
    if flag:
        print(a)
        break
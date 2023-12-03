for a in range(1000):
    flag = True # ЭТОТ А ПО УМОЛЧАНИЮ - ПОДХОДИТ
    
    for x in range(1000):
        if not (
            (x&77 != 0) <=
            (
                (x&12 == 0) <=
                (x&a != 0)
            )
        ):
            flag = False
            break

    
    if flag:
        print(a)
        break
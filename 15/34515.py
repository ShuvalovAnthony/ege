for a in range(1000): # 0 - по умолчанию подходит
    flag = True

    # проверяю все Х для даного А
    for x in range(1000):
        if not ( # условие проигрыша 
            (x&41 != 0) <=
            (
                (x&33 == 0) <=
                (x&a != 0)
            )
        ):
            flag = False
            break

    if flag: # если А - подходит - печатаю
        print(a)
        break # наименьшее

    

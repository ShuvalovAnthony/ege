for a in range(1000): # a = 5
    flag = True # a - по умолчанию подходит

    for x in range(1000): # 0, 1, 2, 3, 4...
        for y in range(1000): # 0, 1, 2, 3, 4...
            if not((3*x +7*y < a) or (x >= y) or (y > 6)):
                flag = False
                break

    if flag:
        print(a)
        break
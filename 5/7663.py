for num in range(100, 1000):
    num = str(num)

    summa_1_2 = int(num[0]) + int(num[1])
    summa_2_3 = int(num[1]) + int(num[2])

    if summa_1_2 > summa_2_3:
        res = str(summa_1_2) + str(summa_2_3)
    else:
        res = str(summa_2_3) + str(summa_1_2)
        
    if res == '1412':
        print(num)
        break
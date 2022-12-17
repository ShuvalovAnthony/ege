for num in range(1000, 9999 + 1):
    num = str(num)

    d1_d2 = int(num[0]) + int(num[1])
    d2_d3 = int(num[1]) + int(num[2])
    d3_d4 = int(num[2]) + int(num[3])

    spisok = sorted([d1_d2, d2_d3, d3_d4])

    if (str(spisok[1]) + str(spisok[2])) == '1517':
        print(num)
        break
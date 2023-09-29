for num in range(9999, 999, -1):
    num = str(num)
    sum12 = int(num[0]) + int(num[1])
    sum23 = int(num[1]) + int(num[2])
    sum34 = int(num[2]) + int(num[3])

    # 3 суммы по возрастанию, срезом берем 2 самых больших (0ое удаляется)
    summs = sorted([sum12, sum23, sum34])[1:]
    res = str(summs[0]) + str(summs[1])

    if res == '1315':
        print(num)
        break


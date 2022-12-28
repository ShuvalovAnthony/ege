for num in range(10**3, 10**4):
    num = str(num)
    sum_1_2 = int(num[0]) + int(num[1])
    sum_2_3 = int(num[1]) + int(num[2])
    sum_3_4 = int(num[2]) + int(num[3])


    nums = sorted([sum_1_2, sum_2_3, sum_3_4])

    nums = sorted([sum_1_2, sum_2_3, sum_3_4])[1:] # [1:] - удалить наим, [:-1:] - удалить наиб

    res = str(nums[0]) + str(nums[1])

    if res == '1215':
        print(num)
        break
    
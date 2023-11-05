for n in range(1_000, 10_000):
    n = str(n)

    sum_12 = int(n[0]) + int(n[1])
    sum_23 = int(n[1]) + int(n[2])
    sum_34 = int(n[2]) + int(n[3])

    nums = sorted([sum_12, sum_23, sum_34])[1:]

    res = str(nums[0]) + str(nums[1])

    if res == '613':
        print(n)
        break



for n in range(1000, 10000): # int
    n = str(n) # str "1234"

    sum_12 = int(n[0]) + int(n[1])
    sum_34 = int(n[2]) + int(n[-1])

    nums = sorted([sum_12, sum_34])

    res = str(nums[0]) + str(nums[1])
    
    if res == "117":
        print(n)
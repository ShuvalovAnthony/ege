def sum_digit(n):
    return sum(int(i) for i in str(n))


def f(n):
    n_bin = bin(n)[2:]
    for i in range(3):
        if sum_digit(int(n_bin, 2))%2 == 0: n_bin += '0'
        else: n_bin += '1'
    return int(n_bin, 2)



# for n in range(15432099, 15432099+1000):
#     if 123456789 <= f(n) <= 1987654321: #  
#         print(n)
        # break
    
    # if n%10**6 == 0: print(n)


start = 15432099
stop = 248456789


print(stop - start + 1)
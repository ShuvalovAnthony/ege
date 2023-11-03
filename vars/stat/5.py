from functools import lru_cache

ost_na_3 = set(bin(i%5)[2:] for i in range(3))
ost_na_5 = set(bin(i%5)[2:] for i in range(5))



# def algo_r(r):
#     bin_n = bin(r)[2:]

#     bin_n_step3 = []
#     for 

# @lru_cache
# def algo(n):
#     n_bin = bin(n)[2:]
#     n_bin += bin(n%3)[2:].zfill(2)
#     new_n = int(n_bin, 2)
#     n_bin += bin(n%5)[2:].zfill(3)
#     return int(n_bin, 2)



# counter = 0

# for i in range(10**9):
#     if 1_111_111_110 <= algo(i) <= 1_444_444_416:
#         counter += 1

# print(counter)
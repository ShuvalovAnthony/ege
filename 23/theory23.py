# # +2 *5


# # 2 -> 50

# 2 -> 10 -> 50

# 2 -> 4 -> 8 -> 10 -> 50

# 2 -> 10 -> 20 -> 40 -> 80

from functools import lru_cache


@lru_cache
def fibo(n):
    if n <= 2: return 1
    return fibo(n - 1) + fibo(n - 2)



# for n in range(1, 400):
#     print(fibo(n))



last = 1
prelast = 1

for n in range(2, 1000):
    current = last + prelast
    print(current)

    prelast = last
    last = current
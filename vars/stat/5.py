from functools import lru_cache


@lru_cache
def algo(n):
    n_bin = bin(n)[2:]

    n_bin += bin(n%3)[2:].zfill(2)

    new_n = int(n_bin, 2)
    n_bin += bin(n%5)[2:].zfill(3)

    return int(n_bin, 2)


counter = 0

for num in range(10000):
    res = algo(num)
    print(res)


print(counter)
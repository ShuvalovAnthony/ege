from functools import lru_cache

@lru_cache
def prime(n):
    for i in range(2, int(n**0.5) + 1):
        if n%i == 0: return False
    return True

@lru_cache
def prime_dels(n):
    dels = []
    for i in range(2, n + 1):
        if n%i == 0:
            if prime(i):
                dels.append(i)
    return dels

@lru_cache
def count_prime(n):
    prost = prime_dels(n)
    count = 0
    for i in prost:
        while (n%i == 0):
            n //= i
            count += 1
    return count



f = open('27__/27_906/27A.txt')
n = f.readline()

nums = [int(i) for i in f]
print(nums)
count = 0

for i in range(len(nums) - 1):
    for j in range(i + 1, len(nums)):
        # print(i, j)
        if (
            ((nums[i] + nums[j])%1111 == 0) and\
            (count_prime(nums[i]*nums[j]) >= 10)
        ):
            count += 1


print(count)
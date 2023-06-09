from functools import lru_cache

# является ли число простым
@lru_cache
def prime(n:int):
    for i in range(2, int(n**0.5) + 1):
        if n%i == 0: return False
    return True


# ВСЕ (включая 1 и само число) делители числа
@lru_cache
def all_delit(n:int):
    deliteli = []
    for i in range(1, int(n**0.5) + 1):
        if n%i == 0:
            deliteli += [i, n//i]
    return sorted(set(deliteli))



# все простые множители числа
@lru_cache
def prime_mnozh(n:int):
    prime_delit = []
    for delitel in all_delit(n):
        if prime(delitel): prime_delit.append(delitel)
    return prime_delit


# разложение на простые множители
@lru_cache
def kolvo_prost_mnpzh(n:int):
    prostie = prime_mnozh(n)[1::]
    count = 0
    for i in prostie:
        while (n%i == 0):
            n //= i
            count += 1  
    return count



f = open('27__/27_906/27B.txt')

nums = f.readline()

nums = [int(i) for i in f]

count = 0

nums_krat_1111 = [i for i in nums if i%1111 == 0]

print(nums_krat_1111)

# for i in range(len(nums)):
#     for j in range(i + 1, len(nums)):
#         if (
#             ((nums[i] + nums[j])%1111 == 0) and\
#             kolvo_prost_mnpzh(nums[i]*nums[j]) >= 10
#         ):
#             count += 1
    


# print(count)
        
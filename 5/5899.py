from itertools import permutations


def prime(n):
    for i in range(2, int(n**0.5) + 1):
        if n%i == 0: return False
    return True


def check(n):
    return 10 <= n <= 99


max_n = 0
max_primes = 0


for n in range(10**2, 10**3):
    digits = str(n)

    temp_primes = 0

    for i in permutations(digits, 2):
        num = int(''.join(i))

        if check(num) and prime(num): temp_primes += 1

    if temp_primes >= max_primes:
        max_primes = temp_primes
        max_n = n

print(max_n)



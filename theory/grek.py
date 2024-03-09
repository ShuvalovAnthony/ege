from decimal import localcontext, Decimal

n = int(input())

def rho_factor(n, cache={}):
    if n in cache:
        return cache[n]
    if n <= 1:
        return []
    if n % 2 == 0:
        return [2] + rho_factor(n // 2)
    
    def gcd(a, b):
        while b:
            a, b = b, a % b
        return a

    def f(x):
        return (x**2 + 1) % n

    factors = []
    x = y = 2
    d = 1
    while d == 1:
        for _ in range(int(n**0.25)):
            x = f(x)
            y = f(f(y))
            d = gcd(abs(x - y), n)
            if d != 1:
                break
        if d == n or d == 1:
            factors.append(n)
            break
        factors.extend(rho_factor(d, cache))
        factors.extend(rho_factor(n // d, cache))
        break
    
    cache[n] = factors
    return factors



def get_all_divisors(n):
    factors = rho_factor(n)
    divisors = set()
    divisors.add(1)
    for i in range(1, 1 << len(factors)):
        divisor = 1
        for j in range(len(factors)):
            if (i >> j) & 1:
                divisor *= factors[j]
        divisors.add(divisor)
    return sorted(list(divisors), reverse=True)


def isqrt(n):
    nd = Decimal(n)
    with localcontext() as ctx:
        ctx.prec = n.bit_length()
        i = int(nd.sqrt())
    if i**2 != n:
        return False
    return i


for div in get_all_divisors(n):
    if (isqrt(div)):
        print(int(div))
        break


# является ли число простым
def prime(n:int):
    for i in range(2, int(n**0.5) + 1):
        if n%i == 0: return False
    return True


def del_na_2(n):
    while n%2 == 0:
        n //= 2
    return n


for i in range(45*10**6, 50*10**6 + 1):
    tmp = del_na_2(i)
    if (tmp**0.25) == int(tmp**0.25):
        if prime(tmp**0.25):
            print(i)
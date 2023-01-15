def simple(n):
    for i in range(2, int(n**0.5)):
        if n%i == 0:
            return False
    return True


for i in range(2422000, 2422080 + 1):
    if simple(i): print(i)
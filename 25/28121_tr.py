def prime(n):
    for i in range(2, int(n**0.5) + 1):
        if n%i == 0:
            return False
    return True

counter = 1

for i in range(2422000, 2422080 + 1):
    if prime(i):
        print(counter, i)
        counter += 1



from fnmatch import fnmatch


def isPrime(n):
    for i in range(2, int(n**0.5) + 1):
        if n%i == 0: return False
    return True


nums = ['']
for i in range(10**4):
    if not isPrime(i): nums.append(str(i))


for i in range(22768, 10**8 + 1, 22768):
    for n in nums:
        mask = f"1{n}03*6*"
        if fnmatch(str(i), mask):
            print(i, n)


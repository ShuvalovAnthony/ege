from time import time

start = time()



def check(num: int):
    for i in range(2, int(num**0.5) + 1):
        if num%i == 0:
            return i + num//i


limit = 5

for num in range(700_001, 10**10):
    res = check(num)
    if res and (res%10 == 8):
        print(num, res)

        limit -= 1

        if not limit: break



print(time() - start)
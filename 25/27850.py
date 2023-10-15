def simple(num: int):
    for i in range(2, num):
        if num%i == 0:
            return False
    return num


nomer = 1

for i in range(245690, 245757):
    if simple(i):
        print(nomer, simple(i))
    nomer += 1
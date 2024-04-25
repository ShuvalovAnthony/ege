def check(num: int):
    deliteli = []
    for i in range(2, int(num**0.5) + 1):
        if (num%i == 0):
            if (i%10 == 8) and (i != 8):
                deliteli.append(i)
            elif ((num//i)%10 == 8) and ((num//i) != 8):
                deliteli.append(num//i)
    if deliteli: return min(deliteli)


limit = 5

for num in range(500000, 10**9):
    res = check(num)
    if res:
        print(num, res)
        limit -= 1
    if not limit:
        break
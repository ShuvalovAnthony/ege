def check(num):
    if num**0.5 != int(num**0.5): return False

    deliteli = set()
    for i in range(2, int(num**0.5) + 1):
        if num%i == 0:
            deliteli.add(i)
            deliteli.add(num//i)
        
        if len(deliteli) > 3: return False

    if len(deliteli) == 3: return max(deliteli)
    return False



for num in range(123456789, 223456789):
    res = check(num)
    if res:
        print(num, res)
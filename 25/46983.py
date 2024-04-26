def f(num: int):
    deliteli = set()

    for i in range(2, int(num**0.5) + 1):
        if num%i == 0:
            deliteli.add(i)
            deliteli.add(num//i)

    if len(deliteli) < 5: return 0

    deliteli = sorted(deliteli)
    return deliteli[-5]



limit = 5

for num in range(46*10**7 + 1, 10**9):
    res = f(num)
    if res:
        print(res)
        limit -= 1

    if not limit: break
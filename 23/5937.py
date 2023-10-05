from functools import cache

@cache
def f(a, b, limit=0):
    limit += (a + 1)%2
    if a > b or limit > 15: return 0 # либо убрав эту строку изменить нижние 2
    if a == b: return 1 # if a == b and limit != 0: return 1
    return f(a + 2, b, limit) +\
        f(a + 3, b, limit) + f(a*2 + 1, b, limit)

print(f(1, 55))

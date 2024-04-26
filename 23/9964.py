from functools import lru_cache

@lru_cache(None)
def f2(s, e, p1='', p2='', valid=False):
    if s > e: return 0
    if s == e: return valid

    count = 0
    count += f2(s+1, e, 'A', p1, valid)
    count += f2(s*3, e, 'B', p1, valid)

    valid = valid or (p2 + p1 + 'C' == 'CAC')
    count += f2(s+5, e, 'C', p1, valid)

    return count

print(f2(3, 69))
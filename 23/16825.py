def f(a, b):
    if (a > b) or (a in (6, 12)): return 0
    elif a == b: return 1
    return f(a + 1, b) + f(a*2, b) + f(a + 3, b)


print(f(3, 16))

import sys

sys.setrecursionlimit(5000)
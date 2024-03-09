import math

N = int(input())

ans = 1
for i in range(1, int(N**0.5) + 1):
    if N % i == 0:
        if N // i % i == 0:
            ans = max(ans, i * i)
        N2 = N // i
        lo = 1
        hi = 1000000000
        while lo < hi:
            mi = (lo + hi) >> 1
            if mi * mi < N2:
                lo = mi + 1
            else:
                hi = mi
        if lo * lo == N2:
            ans = max(ans, N2)

print(ans)

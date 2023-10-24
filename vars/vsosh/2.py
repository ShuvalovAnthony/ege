import math


n = int(input())
k = int(input())


coord = int(math.log(n, 2))
if n == k:
    print(k)
else:
    print(coord + k - 1)

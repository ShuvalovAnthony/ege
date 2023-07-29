res = set()

for n in range(10, 1001):
    n_bin = int(bin(n)[3:], 2)
    res.add(n - n_bin)

print(len(res))
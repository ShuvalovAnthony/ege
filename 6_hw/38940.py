count = 0
for s in range(10, 10**6):
    s = 3*(s//10)
    n = 1
    while s < 221:
        s += 13
        n *= 2
    if n == 128:
        count += 1

print(count)
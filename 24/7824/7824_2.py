from itertools import product


f = open('24/7824/24_7824.txt').read()

combos = [''.join(i) for i in product('ABC', repeat=3)]

count = 0

tmp_count = 0

for i in range(len(f)):
    if f[i:i + 3] not in combos:
        tmp_count += 1
    else:
        count = max(tmp_count + 2, count)
        tmp_count = 0

print(count)







count = 1
max_c = -10**6
for i in range(len(f) - 2):
    if (f[i] + f[i + 1] + f[i + 2]) not in combos:
        count += 1
    else:
        max_c = max(max_c, count)
        count = 1

print(max_c)
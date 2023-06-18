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
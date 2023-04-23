from itertools import product

f = open('24/7356/24_7356.txt').read()


max_len = 0

for start in range(len(f)):
    limit = 6
    tmp_len = 0
    for i in range(start, len(f)):
        if limit == 0:
            max_len = max(tmp_len, max_len)
            break

        if (f[i] in 'CDF') and (f[i + 1] in 'AO'):
            limit -= 1
        
        tmp_len += 1
        
print(max_len)

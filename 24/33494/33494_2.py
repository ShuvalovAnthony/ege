from collections import Counter

f = open('24/33494/24.txt').read()

res = ''

for i in range(len(f) - 1):
    if f[i] == 'E': res += f[i + 1]


print(Counter(res).most_common(1))
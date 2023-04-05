f = open('24/2251/24_2251.txt').read()


for i in range(10**4, 1, -1):
    f = f.replace('D'*i, '_')

f = f.split('_')

res = []

for i in f:
    res.append(i.split('D'))

def max_len(rows: list):
    lens = list(map(len, rows))
    if len(lens) < 3: return sum(lens)
    max_len = 0
    for i in range(len(lens) - 3):
        max_len = max(max_len, sum(lens[i:i + 3]))
    return max_len + 2

answer = 0

for i in res:
    answer = max(answer, max_len(i))

print(answer)

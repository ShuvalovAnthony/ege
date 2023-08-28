f = open('26/2653.py/26_2653.txt')

f.readline()
s = sorted([int(i) for i in f])

a = {0}
for i in s: a |= {x + i for x in a}
ans = [i for i in range(sum(s)) if i not in a]
print(len(ans), max(ans))
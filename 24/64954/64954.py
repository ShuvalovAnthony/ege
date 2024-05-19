f = open("24/64954/24.txt").read()
d = {'A':[],'B':[],'C':[],'D':[],'E':[],'F':[]}
l = 0
maxi = 0
for i in range(len(f)):
    if f[i] in 'ABCDEF':
        d[f[i]].append(i)
        if len(d[f[i]]) > 100:
            l = max(l, d[f[i]][0] + 1)
            del d[f[i]][0]
    maxi = max(maxi, i - l +1)
print(maxi)
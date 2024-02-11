f = open("24/59729/1_24.txt").read()

t_ind = []
min_len = 10**6
for i in range(len(f)):
    if f[i:i + 2] == 'TT': t_ind.append(i)



for i in range(len(t_ind) - 150):
    min_len = min(min_len, t_ind[i + 149] - t_ind[i] + 2)

print(min_len)
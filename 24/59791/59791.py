f = open("24/59791/24.txt").read()


w_indexes = []
min_len = 10**9

for i in range(len(f)):
    if f[i] == 'W': w_indexes.append(i)

for i in range(len(w_indexes) - 130):
    min_len = min(min_len, w_indexes[i + 129] - w_indexes[i] + 1)

print(min_len)


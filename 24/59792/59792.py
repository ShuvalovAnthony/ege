f = open("24/59792/24.txt").read()


t_indexes = []

for i in range(len(f)):
    if f[i] == 'T':
        t_indexes.append(i)

min_dlina = 10**9

for i in range(len(t_indexes) - 100):
    min_dlina = min(
        min_dlina,
        t_indexes[i + 100 - 1] - t_indexes[i] + 1
    )


print(min_dlina)
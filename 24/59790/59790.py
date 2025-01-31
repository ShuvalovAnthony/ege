f = open("24/59790/59790.txt").read()


t_indexes = []


for i in range(len(f)):
    if f[i] == "T":
        t_indexes.append(i)

min_len = 10**7

for i in range(len(t_indexes) - 210):
    left_t = t_indexes[i]
    right_t = t_indexes[i + 209]

    slice = f[left_t:right_t + 1]

    min_len = min(min_len, len(slice))


print(min_len)

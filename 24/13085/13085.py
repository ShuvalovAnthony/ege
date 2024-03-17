f = open('24/13085/24_13085.txt').read()

indexes = []
for i in range(len(f)):
    if (f[i] == 'X') or (f[i] == 'Y'):
        indexes.append(i)

max_len = 0

for i in range(len(indexes) - 4):
    kusok_i_bokovuhi = f[indexes[i]:indexes[i + 3] + 1]
    kusok_bez_bokovuh =  f[indexes[i] + 1:indexes[i + 3]]
    if kusok_bez_bokovuh.count('X') == kusok_bez_bokovuh.count('Y'):
        max_len = max(max_len, len(kusok_bez_bokovuh))


print(max_len)
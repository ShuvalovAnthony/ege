f = open('24/27690/zadanie24_1.txt').read()

max_dlina = 0
tmp_dlina = 1

for i in range(len(f) - 1):
    if f[i + 1] != f[i]:
        tmp_dlina += 1
    else:
        max_dlina = max(max_dlina, tmp_dlina)
        tmp_dlina = 1


print(max_dlina)
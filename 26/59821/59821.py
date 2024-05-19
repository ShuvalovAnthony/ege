f = open("26/59821/26_59821.txt")

n = int(f.readline())

details = []

shlif = []
pokras = []

for i in range(1, n + 1):
    tShlif, tPokras = [int(i) for i in f.readline().split()]
    if tShlif < tPokras:
        shlif.append([tShlif, i])
    else:
        pokras.append([tPokras, i])

shlif, pokras = sorted(shlif), sorted(pokras)

print(shlif[-1][-1], len(shlif) - 1)

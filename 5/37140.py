a = []

for n in range(1, 100):
    n_bin = bin(n)[2:] # перевод в двоичную систему

    if n%2 == 0:
        n_bin = "1" + n_bin + "0"
    else:
        n_bin = "11" + n_bin + "11"

    r = int(n_bin, 2)

    if r > 52:
        a.append(r)

print(min(a))
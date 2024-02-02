f = open('24/59847/24.txt').read()



dlini = []
temp_dlina = 0


for i in range(len(f) - 1):
    if f[i] + f[i + 1] == 'WW':
        dlini.append(temp_dlina)
        temp_dlina = 0
    else:
        temp_dlina += 1

# print(dlini)


max_dlina = 0

for i in range(len(dlini) - 99):
    max_dlina = max(
        max_dlina,
        sum(dlini[i:i + 99])
    )


print(max_dlina + 200)
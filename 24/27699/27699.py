f = open("24/27699/27699.txt").read().replace("LDR", "___")



temp_dlina = 0
max_dlina = 0

for i in range(len(f)):
    if f[i] == "_":
        temp_dlina += 1
    else:
        if f[i] == 'L' and f[i + 1] == 'D':
            max_dlina = max(max_dlina, temp_dlina + 2)
            temp_dlina = 0
        elif f[i] == 'L':
            max_dlina = max(max_dlina, temp_dlina + 1)
            temp_dlina = 0
        else:
            max_dlina = max(max_dlina, temp_dlina)
            temp_dlina = 0


print(max_dlina)

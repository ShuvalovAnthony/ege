f = open('ege/24/27689/24.txt').readline()


etalon = 'XYZ'
max_dlina = 0

for i in range(len(f)):
    counter = 0
    nomer = 0
    if f[i] == 'X':
        for j in range(i, len(f)):
            if f[j] == etalon[nomer%3]:
                counter += 1
            else:
                break
            nomer += 1
        max_dlina = max(max_dlina, counter)

print(max_dlina)




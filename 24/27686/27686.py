f = open('ege/24/27686/24.txt').readline()


max_dlina = 0

'XYXXYYXYZYZYZZYYZXYXYXYYXYX'


for i in range(len(f)):
    if f[i] == 'X':
        counter = 1
        for j in range(i + 1, len(f)):
            if f[j] == f[j - 1]:
                counter += 1
            else:
                max_dlina = max(max_dlina, counter)
                break

print(max_dlina)



f = open('ege/24/27421/24_demo.txt').readline()


max_dlina = 0

for i in range(len(f)):
    counter = 1
    for j in range(i + 1, len(f)):
        if f[j] != f[j - 1]:
            counter += 1
        else:
            max_dlina = max(max_dlina, counter)
            break

print(max_dlina)



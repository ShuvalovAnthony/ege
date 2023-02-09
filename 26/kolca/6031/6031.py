# задача с сайта https://kompege.ru/

f = open('26/kolca/6031/26.txt')

diameters = sorted(set([int(i) for i in f]))


print([diameters[-1]])
max_d = 0
max_count = 0


for i in range(len(diameters)):
    tmp_count = 1
    last_d = diameters[i]
    for j in range(i + 1, len(diameters)):
        if diameters[j] >= last_d + 6:
            tmp_count += 1
            last_d = diameters[j]

    if tmp_count >= max_count:
        max_count = tmp_count
        max_d = diameters[i]

print(max_count, max_d)

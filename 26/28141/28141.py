f = open("26/28141/28141.txt")

free_space, n = map(int, f.readline().split())

archieves = sorted([int(i) for i in f])

saved = []

for archieve in archieves:
    if free_space - archieve >= 0:
        free_space -= archieve
        saved.append(archieve)

if max(saved) + free_space in archieves:
    print(len(saved), max(saved) + free_space)
else:
    print("PUPUPUU")

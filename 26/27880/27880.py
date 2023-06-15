f = open('26/27880/27880.txt')

free_space, n = map(int, f.readline().split())

archieves = sorted([int(i) for i in f])

saved = []

for archieve in archieves:
    if free_space - archieve >= 0:
        free_space -= archieve
        saved.append(archieve)

print(len(saved), max(saved), free_space)


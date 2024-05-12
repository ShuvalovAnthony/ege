f = open("26/16390/26_16390.txt")

free_space, n = map(int, f.readline().split())

posilki = sorted([int(i) for i in f])


counter = 0
maxPosilka = 0

for posilka in posilki:
    if posilka <= free_space:
        counter += 1
        free_space -= posilka
        maxPosilka = posilka


print('колво посылок', counter)
print('макс посылка', maxPosilka)

print(free_space, posilki[::-1])
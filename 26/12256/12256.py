f = open("26/12256/26_12256.txt")

free_space, n = map(int, f.readline().split())

items = sorted([int(i) for i in f])


itemsCounter = 0
maxItem = 0


for item in items:
    if item <= free_space:
        itemsCounter += 1
        free_space -= item
        maxItem = item

# 32 maxitem
print(free_space)
print(items[::-1])
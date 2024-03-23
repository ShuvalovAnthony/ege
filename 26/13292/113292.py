f = open("26/13292/26_13292.txt")

n, k = map(int, f.readline().split())

details = sorted([int(i) for i in f])[:k]

last = details[-1]
left = []
right = []

for i in range(len(details)):        
    if details[i]%2 == 0:
        left.append(details[i])
    else:
        right.append(details[i])

right = sorted(right, reverse=True)


if last%2 == 0:
    print("Posled", left.index(last) + 1)
    print("Summa", sum(right))
else:
    print("Posled", len(left) + right.index(last) + 1)
    print("Summa", sum(right[right.index(last) + 1:]))

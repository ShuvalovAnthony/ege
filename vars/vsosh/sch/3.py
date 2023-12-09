n = int(input())
m = int(input())
k = int(input())
c = int(input())


fragment = [i for i in range(1, k + 1)]
row = fragment*(m//k + 1 + n)

counter = 0

for i in range(n):
    counter += row[i:m + i].count(c)

print(counter)
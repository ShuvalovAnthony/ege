'''s = int(input())
n = 1
while s < 51:
    s = s + 5
    n = n * 2
print(n)'''


for s in range(10**6):
    start_s = s
    n = 1

    while s < 51:
        s += 5
        n *= 2

    if n == 64:
        print(start_s)
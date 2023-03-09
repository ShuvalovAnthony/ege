def f(n: int):
    if n == 0: return 0
    elif n%2 == 0: return f(n//2)
    return 1 + f(n - 1)

count = 0

for i in range(1, 1001):
    if f(i) == 3:
        count += 1

print(count)
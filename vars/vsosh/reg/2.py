n = int(input())

digits = []


for digit in range(2, 10):
    while n%digit == 0:
        digits.append(str(digit))
        n //= digit

if n == 1: print(1 or ''.join(digits))
else: print(-1)
from string import digits, ascii_lowercase

alph = digits + ascii_lowercase[:8]

res = set()

for x in alph:
    for y in range(2, 32):
        try:
            num = int('5' + x + alph[y] + 'c', 16) +\
            int('8' + x + x + '7', y)
            res.add(num)
        except:
            ...

print(res)
print(len(res))

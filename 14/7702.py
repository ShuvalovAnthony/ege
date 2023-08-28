from string import digits, ascii_lowercase

alph = digits + ascii_lowercase[:8]

res = set()

for x in alph:
    for y in range(2, 18):
        try:
            num = int('5' + x + alph[y] + 'a', 18) +\
            int('18' + x + '7', y)
            res.add(num)
        except:
            ...

print(len(res))
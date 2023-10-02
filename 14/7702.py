from string import digits, ascii_lowercase

alph = digits + ascii_lowercase[:8]

result = set()

for x in alph:
    for y in range(2, 32):
        try:
            res = int('5' + x + alph[y] + 'a', 18) +\
            int('18' + x + '7', y)
            result.add(res)
        except:
            pass

print(len(result))

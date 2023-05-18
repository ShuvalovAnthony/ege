f = open('24/8510/24_8510.txt').read()


f = f.replace('N', ' ')\
    .replace('O', ' ')\
    .replace('P', ' ')


for i in range(100, 1, -1):
    f = f.replace(' '*i, '  ')

print(max(
    [len(i) for i in f.split('  ')]
))
f = open('24/8510/24_8510.txt').read()


f = f.replace('N', ' ')\
    .replace('O', ' ')\
    .replace('P', ' ')



print(
    max(
    [len(i.strip()) for i in f.split('  ')]
) + 2
)
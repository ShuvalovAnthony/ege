f = open('24/7723/24_7723.txt').read()


f = f.replace('R', 'D')\
    .replace('8', '1')\
    .replace('11D', '-')\
    .replace('D', ' ').replace('1', ' ')

print(
    max(len(i) for i in f.split())
)




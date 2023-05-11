from string import ascii_uppercase, digits

f = open('24/7688/24_7688.txt').read().upper()


for letter in (ascii_uppercase + digits):
    if letter not in 'XAYT':
        f = f.replace(letter, ' ')

f = f.replace('TXA', '---')\
    .replace('XA', '--')\
    .replace('XY', '--')\
    .replace('X', ' ')\
    .replace('A', ' ')\
    .replace('Y', ' ')\
    .replace('T', ' ')


print(
    max([len(i) for i in f.split()])
)

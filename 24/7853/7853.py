from string import ascii_uppercase, digits

f = open('24/7853/24_7853.txt').read()


for letter in (ascii_uppercase + digits):
    if letter in 'NOT':
        f = f.replace(letter, '*')
    else:
        f = f.replace(letter, '-')

print(
    max([len(i) for i in f.split('*-*')]) + 4
)
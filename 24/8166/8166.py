from string import ascii_uppercase

f = open('24/8166/24_8166.txt').read()

for letter in ascii_uppercase:
    if letter in 'ABC':
        f = f.replace(letter, '-')
    else:
        f = f.replace(letter, ' ')



print(
    max(
        [len(i) for i in f.split()]
    )//2
)
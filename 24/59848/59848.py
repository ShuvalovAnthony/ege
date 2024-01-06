from string import ascii_uppercase

f = open("24/59848/24_59848.txt").read()

alph = ascii_uppercase[:14]

for i in ascii_uppercase:
    if i not in alph:
        f = f.replace(i, ' ')


print(max(
    [len(i) for i in f.split()]
))

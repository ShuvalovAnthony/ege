f = open('10/33755/33755.txt').read()

slova = f.split()

for i in slova:
    if 'шерст' in i:
        print(i)
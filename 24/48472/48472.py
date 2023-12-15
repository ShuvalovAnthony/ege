f = open('24/48472/24.txt').read()

f = (
    f.replace('O', 'A')
    .replace('D', 'C')
    .replace('F', 'C')
    .replace('AAC', '_')
    .replace('A', ' ')
    .replace('C', ' ')
    )


print(max([len(i) for i in f.split()]))
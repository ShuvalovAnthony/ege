from itertools import product

f = open('24/7624/24_7624.txt').read()


combos = [''.join(i) for i in product('XYZ', repeat=2)]

for i in combos:
    f = f.replace(i, ' ')

len_strok = [len(i) for i in f.split()]

# проверяем что макс не с краев
print(max(len_strok), len_strok[0], len_strok[-1])

print('Otvet', max(len_strok) + 2)
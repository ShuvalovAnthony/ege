from itertools import product

def f(s):
    while '11' in s:
        if '112' in s:
            s = s.replace('112','6',1)
        else:
            s = s.replace('11','3',1)
    return s

max_summa_cifr = 0

for a in product('12', repeat=14):
    if a.count('1') == 10 and a.count('2') == 4:
        s = ''.join(a)
        s = f(s)

        summa_cifr = sum([int(i) for i in s])

        if summa_cifr > max_summa_cifr:
            max_summa_cifr = summa_cifr


print(max_summa_cifr)
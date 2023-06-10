from itertools import product

def redaktor(s):
    while '12' in s:
        s = s.replace('12','4',1)
    return s

def summa_cifr(s):
    return sum([int(i) for i in s])



flag = False

for kolvo_dvoek in range(10):
    if flag: break
    for a in product('12', repeat=(10 + kolvo_dvoek)):
        if a.count('1') == 10:
            s = ''.join(a)
            
            s = redaktor(s)

            if summa_cifr(s) == 25:
                print(kolvo_dvoek)
                flag = True
                break
f = open('24/36879/inf_26_04_21_24.txt')

stroki = []

for i in f:
    if i.count('G') < 25:
        stroki.append(i.rstrip('\n'))


def max_rasst(stroka):
    import string
    max_rasst = 0
    for i in string.ascii_uppercase:
        if stroka.count(i) >= 2:
            first = stroka.index(i)
            last = len(stroka) - stroka[::-1].index(i) - 1
            max_rasst = max(max_rasst, last - first)
    return max_rasst


for stroka in stroki:
    print(max_rasst(stroka))

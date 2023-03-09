f = open('24/35998/inf_26_04_21_24.txt')

stroki = []


for i in f:
    s = i.rstrip('\n')
    if s.count('A') < 25:
        stroki.append(s)


print(stroki, len(stroki))
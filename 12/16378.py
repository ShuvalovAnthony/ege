summs = []

for n in range(4, 1000):
    s = '8' + '4'*n

    while ('11' in s) or ('444' in s) or ('8888' in s):
        s = s.replace('11', '4', 1)
        s = s.replace('444', '88', 1)
        s = s.replace('8888', '1', 1)

    summs.append(sum([int(i) for i in s]))


print(max(summs))
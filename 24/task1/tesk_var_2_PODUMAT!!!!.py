s = open('24/task1/24.txt').read()


sp = []

for i in range(len(s)):
    if i == 'F':
        sp.append('F' + str(i))
    elif i == 'A':
        sp.append('A' + str(i))

print(sp)
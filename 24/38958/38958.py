f = open('24/38958/24.txt').read()


def max_pair(lens):
    maximum = 0
    for i in range(len(lens) - 1):
        maximum = max(maximum, lens[i] + lens[i + 1])
    return maximum


for i in range(10000, 1, -1):
    f = f.replace('A'*i, ' ')

stroki = f.split()

vse_dlini = []


for stroka in stroki:
    lens = [len(i) for i in stroka.split('A')]
    vse_dlini.append(max_pair(lens) + 1)
    

print(max(vse_dlini))
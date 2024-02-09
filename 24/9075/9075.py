f = open("24/9075/24_9075.txt").read()

for i in '3579':
    f = f.replace(i, '1')

for i in '2468':
    f = f.replace(i, '0')


f = f.replace('10', ' ').replace('01', ' ')


print(
    max(
        [len(stroka) for stroka in f.split()]
    ) + 2
)
s = '>' + '3'*20 + '2'*10 + '11111222221111122222' + '3'*10

while ('>1' in s) or ('>2' in s) or ('>3' in s):
    if '>1' in s:
        s = s.replace('>1', '22>', 1)
    elif '>2' in s:
        s = s.replace('>2', '2>', 1)
    elif '>3' in s:
        s = s.replace('>3', '1>', 1)

s = s.replace('>', '')

summa_cifr = 0

for i in s:
    summa_cifr += int(i)

print(summa_cifr)
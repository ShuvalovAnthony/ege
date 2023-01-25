f = open('24/46982/24.txt').read()

stroki = f.split('E')

count = 0

for i in stroki:
    if ('F' not in i) and (len(i) >= 10):
        count += 1

print(count)
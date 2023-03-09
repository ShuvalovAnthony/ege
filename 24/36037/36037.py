f = open('24/36037/24.txt').read().replace('XZZY', '_') # str

posled = list(map(len, f.split('_')))


print(max(posled) + 6)
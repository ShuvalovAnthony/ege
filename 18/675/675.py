# f = open('18/675/675.txt')

# res = ''

# for i in f: res += str(int(i)%2)

print(max([len(i) for i in ''.join([str(int(i)%2) for i in open('18/675/675.txt')]).split('0')]))


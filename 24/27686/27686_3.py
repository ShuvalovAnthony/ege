f = open('24/27686/24.txt').readline()

f = f.replace('Y', 'Z').split('Z')

max_dlina = 0

for i in f:
    max_dlina = max(max_dlina, len(i))


print(max_dlina)

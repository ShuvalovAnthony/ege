f = open('ege/24/27686/24.txt').readline()


f = f.split('Y')

max_dlina = 0

for i in f:
    tmp_list = i.split('Z')
    for j in tmp_list:
        max_dlina = max(max_dlina, len(j))


print(max_dlina)
f = open("24/ya123/24.txt").read()


e_indexes = []

for i in range(len(f)):
    if f[i] == 'E':
        e_indexes.append(i)


min_kolvo = 10**6


for i in range(len(e_indexes) - 239):
    len_temp_s = e_indexes[i + 239] - e_indexes[i] + 1
    min_kolvo = min(min_kolvo, len_temp_s)

print(min_kolvo)
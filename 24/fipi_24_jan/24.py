f = open("24/fipi_24_jan/24_2024.txt").read()

t_indexes = []

kolvo_t = 100


for i in range(len(f)):
    if f[i] == 'T':
        t_indexes.append(i)

max_dlina = 0

for i in range(len(t_indexes) - kolvo_t):
    left_index = t_indexes[i]
    right_index = t_indexes[i + kolvo_t - 1]

    if  right_index - left_index + 1 > max_dlina:
        max_dlina = right_index - left_index + 1


print(max_dlina)
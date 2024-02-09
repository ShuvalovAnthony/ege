f = open("24/13100/24_13100.txt").read()


index_c = []
index_d = []

for i in range(len(f)):
    if f[i] == 'C': index_c.append(i)
    if f[i] == 'D': index_d.append(i)

all_indexes = sorted(index_c + index_d)


def check_temp(temp_posled):
    return temp_posled.count("C") == temp_posled.count("D")


max_dlina = 0

for i in range(len(all_indexes) - 6): # 0    1 2 3 4   5
    temp_posled = f[all_indexes[i] + 1: all_indexes[i+5]]
    if check_temp(temp_posled):
        left = all_indexes[i]
        right = all_indexes[i + 6]
        stroka = f[all_indexes[i] + 1: all_indexes[i+5]]
        temp_dlina = len(stroka)

        if temp_dlina > max_dlina:
            max_dlina = temp_dlina
            answ = stroka


print(max_dlina)
print(answ, answ.count("C"), answ.count("D"), len(answ))
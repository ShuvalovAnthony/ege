f = open("24/13100/24_13100.txt").read()


all_indexes = []

for i in range(len(f)):
    if (f[i] == 'C') or (f[i] == 'D'): all_indexes.append(i)


def check_temp(temp_posled):
    return temp_posled.count("C") == temp_posled.count("D")

max_dlina = 0

for i in range(len(all_indexes) - 5): # 0    1 2 3 4   5
    temp_posled = f[all_indexes[i] + 1: all_indexes[i+5]]
    if check_temp(temp_posled):
        
        if len(temp_posled) > max_dlina:
            max_dlina = len(temp_posled)
            answ = temp_posled


print(max_dlina)
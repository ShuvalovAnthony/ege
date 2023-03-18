f = open('26/podarki/5988/data.txt')

# R 
# G -
# B <<

data = []

# битый файл - цикл для создания нормального массива, 1, 2, 3 - цвета RGB (порядок для задачи не важен)
for i in f:
    try:
        s = i.split()
        nums = int(s[0])
        color = s[1]
        if color == "—":
            data.append((int(s[0]), 1))
        else:
            data.append((int(s[0]), 2))
    except:
        data.append((int(i), 3))


data = sorted(data, key=lambda x:x[0])

uniq_data = []
for i in data:
    if i not in uniq_data:
        uniq_data.append(i)

answ = [[0, 0] for i in range(len(uniq_data))]


for i in range(len(uniq_data)):
    max_side_len = 10**6
    max_count = 0

    for j in range(0, i):
        if (uniq_data[j][0] <= uniq_data[i][0] - 7) and \
            (uniq_data[j][1] != uniq_data[i][1]):
            if answ[j][0] > max_count or \
                (answ[j][0] == max_count and answ[j][1] < max_side_len):
                max_count, max_side_len = answ[j]
    
    if max_side_len == 10**6:
        max_side_len =  uniq_data[i][0]
    answ[i] = [max_count + 1, max_side_len]

print(*answ[-1])



# # ЖАДНЫЙ АЛГОРИТМ (НЕПРАВИЛЬНЫЙ!!!) - 1 балл из 2х за задачу

# max_side_len = 0
# max_count = 0

# for i in range(len(uniq_data)):
#     temp_count = 1
#     last_side = uniq_data[i]

#     for j in range(i + 1, len(uniq_data) - 1):
#         if (uniq_data[j][0] >= last_side[0] + 7) and \
#             (last_side[1] != uniq_data[j][1]):
#                 temp_count += 1
#                 last_side = uniq_data[j]
    
#     if temp_count > max_count:
#         max_count = temp_count
#         max_side_len = uniq_data[i][0]

# print(max_count, max_side_len)
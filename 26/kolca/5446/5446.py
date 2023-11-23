f = open('26/kolca/5446/26.txt')

diametres = []
for i in f:
    d, s = map(int, i.split())
    diametres.append([d, d - 2*s])

diametres = sorted(diametres, key=lambda x: (x[0], x[1]))

uniq_data = []
for i in diametres:
    if i not in uniq_data:
        uniq_data.append(i)

max_count = 0
max_diameter = 0


for i in range(len(uniq_data)):
    temp_count = 1

    vnutr_dVnesh = uniq_data[i][0] # внешний D внутренний трубы
    last_vnesh = vnutr_dVnesh

    for j in range(i + 1, len(uniq_data)):
        vnesh_dVnesh = uniq_data[j][0] # внешний D внешний трубы
        vnesh_dvnutr = uniq_data[j][1] # внутренний

        if vnesh_dvnutr >= last_vnesh + 3:
            temp_count += 1
            last_vnesh = vnesh_dVnesh

    
    if temp_count >= max_count:
        max_count = temp_count
        max_diameter = uniq_data[i][0]


print(max_count, max_diameter)
f = open('26/7826/26_7826.txt')

k, n = [int(i) for i in f.readline().split()] # k - колво аттракционов

visitors = sorted(
    [list(map(int, i.split())) for i in f],
    key=lambda x: (x[0], -x[1])
    )

stops = [-1]*k # время когда освободится аттракцион
visitors_counter = 0

last_attrs_number = 0

last_start = 0

for start, stop in visitors:
    for attr_index in range(k):
        if start == last_start:
            visitors_counter += 1
            break
        if start >= stops[attr_index]:
            visitors_counter += 1
            stops[attr_index] = stop + 1
            last_attrs_number = attr_index + 1 # тк отсчет в человеческих координатах
            last_start = start
            break

print(visitors_counter, last_attrs_number)
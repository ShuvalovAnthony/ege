f = open("ege/26/69934/69934.txt")

n, m, k = [int(i) for i in f.readline().split()]


data = {i:[] for i in range(1, k + 1)}


for row_ in f:
    row, seat = [int(i) for i in row_.split()]
    data[seat].append(row)

min_len = 10**6
res_v_row_seats = []
res_v_row = 0


for v_row, seats in data.items():
    # если весь вертикальный ряд пустой - сажаем на последнее место😊
    if not seats: 
        print(v_row, m)
    else:
        if len(seats) <= min_len:
            min_len = len(seats)
            res_v_row_seats = seats
            res_v_row = v_row

# print(res_v_row, max(res_v_row_seats) + 1)

    


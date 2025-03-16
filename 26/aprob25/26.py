f = open("ege/26/aprob25/26_20910.txt")

n, m, k = [int(i) for i in f.readline().split()]


closest_seats = [m]*k

for row in f:
    h_row, v_row = [int(i) for i in row.split()]
    closest_seats[v_row - 1] = min(closest_seats[v_row - 1], h_row - 1)


max_dist = 0
min_left_index = k

for i in range(len(closest_seats) - 1):
    left, right = closest_seats[i], closest_seats[i + 1]
    
    temp_max_dist = min(left, right)

    if temp_max_dist > max_dist:
        max_dist = temp_max_dist
        min_left_index = i + 1

print(max_dist, min_left_index)

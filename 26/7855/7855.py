f = open('26/7855/26_7855.txt')


K = int(f.readline())
N = int(f.readline())


clients = [list(map(int, i.split())) for i in f]


rooms = {
    # start, stop, waiting
    i: {
        'start': 0,
        'stop': 0,
        'free': True
    } for i in range(K)
}


def choose_room(start, stop):
    choosen_number = None
    prostoi = 10**6
    min_free_time = 10**6
    waited = False
    for room_num in range(K - 1, -1, -1):
        if (
            start > rooms[room_num]['stop'] and rooms[room_num]['free']
            ):
            if rooms[room_num]['stop'] - start < prostoi:
                prostoi = rooms[room_num]['stop'] - start
                choosen_number = room_num

    if not choosen_number:
        waited = True
        for room_num in range(K):
            tmp = start - rooms[room_num]['stop']
            if tmp < min_free_time:
                min_free_time = tmp
                choosen_number = room_num
    
    rooms[choosen_number]['start'] = start
    rooms[choosen_number]['stop'] = stop + 30

    if waited:
        return min_free_time + 30, choosen_number
    return None, choosen_number


max_time = -1
last_num = 0

for start, stop in clients:
    
    a, b = choose_room(start, stop)
    print(a, b)
    if a:
        max_time = max(max_time, a)
    last_num = b
print(rooms)
print(a, b)


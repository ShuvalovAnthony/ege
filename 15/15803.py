def a(start, stop, x):
    return start <= x <= stop

max_dlina = -1

for start in range(-100, 100):
    for stop in range(-100, 100):
        flag = True

        for x in range(-100, 100):
            if not ((a(start, stop, x) <= (x**2 <= 100)) and\
                 ((x**2 <= 64) <= a(start, stop, x))):
                 flag = False
                 break

        if flag:
            max_dlina = max(max_dlina, abs(start - stop))

print(max_dlina)
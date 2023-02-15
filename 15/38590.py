from itertools import combinations

def d(x):
    return 17 <= x <= 58

def c(x):
    return 29 <= x <= 80

def a(start, stop, x):
    return start <= x <= stop


min_dlina = 10**6

coords = combinations([17, 29, 58, 80], 2)

for start, stop in coords:
    flag = True
    
    for x in range(0, 100):
        if not (d(x) <= (((not c(x)) and (not a(start, stop, x))) <= (not d(x)))):
            flag = False
            break

    if flag:
        min_dlina = min(min_dlina, stop - start)

print(min_dlina)

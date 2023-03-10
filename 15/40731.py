from itertools import combinations

def p(x):
    return 19 <= x <= 84

def q(x):
    return 4 <= x <= 51

def a(start, stop, x):
    return start <= x <= stop


min_dlina = 10**6

coords = combinations([4, 19, 51, 84], 2)


for start, stop in coords:
    flag = True
    
    for x in range(0, 100):
        if not ((not q(x)) or p(x) or a(start, stop, x)):
            flag = False
            break

    if flag:
        min_dlina = min(min_dlina, stop - start)

print(min_dlina)

            
            
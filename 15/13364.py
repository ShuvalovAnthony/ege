from itertools import combinations

def p(x):
    return 130 <= x <= 171

def q(x):
    return 150 <= x <= 185

def a(x, start, stop):
    return start <= x <= stop


coords = combinations(
    sorted([150, 130, 171, 185]),
    2
    )

min_dlina = 10**6

for start, stop in coords:
    flag = True

    for x in range(0, 500):
        ()
        if not ((p(x)) <= (((q(x)) and (not a(x, start, stop))) <= (not p(x)))):
            flag = False
            break

    if flag:
        min_dlina = min(min_dlina, stop - start)
    
print(min_dlina)
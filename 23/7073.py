def f(start, stop):
    if start > stop: return 0
    elif start == stop: return 1

    if start < 0: 
        return f(start**2, stop) + f(start + 3, stop)
    if abs(start) == 1:
        return  f(start*2, stop) + f(start + 3, stop)
    if start == 0:
        return  f(start + 3, stop)
    
    return f(start**2, stop) + f(start*2, stop) +\
    f(start + 3, stop)


summa = 0
for start in range(-20, 20):
    summa += f(start, 20)

print(summa)
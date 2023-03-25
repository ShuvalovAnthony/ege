counter = 0

for a in range(1, 10**6):
    for x in range(1, 10**6):
        flag = True
        if not (
            (a%25 == 0) and
            (
            ((x%24 == 0) and (x%75 == 0)) <= (x%a == 0)
            )
        ):
            flag = False
            break
    if flag:
        counter += 1
    


print(counter)
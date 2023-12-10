counter = 0

for a in range(1, 10**3):
    flag = True

    for x in range(1, 10**3):
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
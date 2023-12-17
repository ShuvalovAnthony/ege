counter = 0

for a in range(-100, 100):
    flag = True

    for x in range(100):
        for y in range(100):
            if not(
                (
                    (x < a) <= (x**2 < 81)
                ) and
                (
                    (y**2 <= 36) <= (y <= a)
                )
            ):
                flag = False


    counter += flag


print(counter)
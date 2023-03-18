def img_weight_in_kb(x, y):
    return x*y*12/1024/8

for x in range(1, 1000):
    for y in range(1, 1000):
        if (
            (img_weight_in_kb(x, y) <= 320) and
            y*4 == x*3
        ):
            print(x, y, x*y)

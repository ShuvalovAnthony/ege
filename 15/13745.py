def check(a):
    for x in range(1000):
        for y in range(1000):
            if not (
                ((x <= 9) <= (x**2 <= a)) and 
                ((y**2 <= a) <= (y <= 9))
            ): return False
    
    return True


for a in range(1000):
    if check(a):
        print(a)


# способ 2

# from itertools import product

# for a in range(1000):
#     flag = True

#     for x, y in product(range(1000), range(1000)):
#         if not (
#             ((x <= 9) <= (x**2 <= a)) and 
#             ((y**2 <= a) <= (y <= 9))
#         ):
#             flag = False
#             break

#     if flag:
#         print(a)
def f20(h1, h2, step): #p1 v2 p3 v4 p5
    if (h1 + h2 >= 47) and (step == 4): 
        return True
    elif (
            ((h1 + h2 >= 47) and (step < 4)) or
            ((h1 + h2 < 47) and (step == 4))
        ): return False

    if step%2 == 0:
        return  (f20(h1 + 1, h2 + 2, step + 1) and
                f20(h1 + 2, h2 + 1, step + 1) and
                 f20(h1 * 2, h2, step + 1) and
                 f20(h1, h2 * 2, step + 1))
    
    return (f20(h1 + 1, h2 + 2, step + 1) or
         f20(h1 + 2, h2 + 1, step + 1) or
         f20(h1 * 2, h2, step + 1) or
         f20(h1, h2 * 2, step + 1))


for h2 in range(1, 37):
    if f20(10, h2, 1):
        print(h2)

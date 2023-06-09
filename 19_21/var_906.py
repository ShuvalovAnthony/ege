def f19(s1, s2, step=1):
    if (s1*s2 >= 455) and (step == 3): return 1
    elif ((s1*s2 < 455) and (step == 3)) or (s1*s2 >= 455): return 0
    return f19(s1 + 1, s2, step + 1) or f19(s1*2, s2, step + 1) or\
    f19(s1, s2 + 1, step + 1) or f19(s1, s2*2, step + 1)
    

for s2 in range(1, 91):
    if f19(5, s2):
        print(s2)
        break



# def f20(s1, s2, step=1):
#     if (s1*s2 >= 455) and (step == 3): return 1
#     elif ((s1*s2 < 455) and (step == 3)) or (s1*s2 >= 455): return 0
#     return f20(s1 + 1, s2, step + 1) or f20(s1*2, s2, step + 1) or\
#     f20(s1, s2 + 1, step + 1) or f20(s1, s2*2, step + 1)
    

# for s2 in range(1, 91):
#     if f20(5, s2):
#         print(s2)
#         break
def f19(s1, s2, step=1): # p-1 v-2 p-3 v-4
    if (max(s1, s2) >= 479) and (step == 3): return 1
    elif (((max(s1, s2) < 479) and (step == 3)) or\
          ((max(s1, s2) >= 479) and (step < 3))
    ): return 0

    if step%2:
        return f19(s1 + 1, s2, step + 1) and\
        f19(s1 + 3, s2, step + 1) and\
        f19(s1*2, s2, step + 1) and\
        f19(s1, s2 + 1, step + 1) and\
        f19(s1, s2 + 3, step + 1) and\
        f19(s1, s2*2, step + 1)
    
    return f19(s1 + 1, s2, step + 1) or\
    f19(s1 + 3, s2, step + 1) or\
    f19(s1*2, s2, step + 1) or\
    f19(s1, s2 + 1, step + 1) or\
    f19(s1, s2 + 3, step + 1) or\
    f19(s1, s2*2, step + 1)


for s2 in range(1, 479):
    if f19(239, s2):
        print(s2)
        break

print('-------')

def f20(s1, s2, step=1): # p-1 v-2 p-3 v-4
    if (max(s1, s2) >= 479) and (step == 4): return 1
    elif (((max(s1, s2) < 479) and (step == 4)) or\
          ((max(s1, s2) >= 479) and (step < 4))
    ): return 0

    if step%2 == 0:
        return f20(s1 + 1, s2, step + 1) and\
        f20(s1 + 3, s2, step + 1) and\
        f20(s1*2, s2, step + 1) and\
        f20(s1, s2 + 1, step + 1) and\
        f20(s1, s2 + 3, step + 1) and\
        f20(s1, s2*2, step + 1)
    
    return f20(s1 + 1, s2, step + 1) or\
    f20(s1 + 3, s2, step + 1) or\
    f20(s1*2, s2, step + 1) or\
    f20(s1, s2 + 1, step + 1) or\
    f20(s1, s2 + 3, step + 1) or\
    f20(s1, s2*2, step + 1)


for s2 in range(1, 479):
    if f20(239, s2):
        print(s2)


print('-------')

def f21(s1, s2, step=1): # p-1 v-2 p-3 v-4
    if (max(s1, s2) >= 479) and (step in (3, 5)): return 1
    elif (((max(s1, s2) < 479) and (step == 5)) or\
          ((max(s1, s2) >= 479))
    ): return 0

    if step%2:
        return f21(s1 + 1, s2, step + 1) and\
        f21(s1 + 3, s2, step + 1) and\
        f21(s1*2, s2, step + 1) and\
        f21(s1, s2 + 1, step + 1) and\
        f21(s1, s2 + 3, step + 1) and\
        f21(s1, s2*2, step + 1)
    
    return f21(s1 + 1, s2, step + 1) or\
    f21(s1 + 3, s2, step + 1) or\
    f21(s1*2, s2, step + 1) or\
    f21(s1, s2 + 1, step + 1) or\
    f21(s1, s2 + 3, step + 1) or\
    f21(s1, s2*2, step + 1)


for s2 in range(1, 479):
    if f21(239, s2):
        print(s2)
        break
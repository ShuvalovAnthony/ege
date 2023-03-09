# 1 - p

# s1 s2 - колво камней в кучах 1 и 2 соотв


def f(s1, s2, step=1): # 1p 2v 3p 4v 5p 6v
    if (s1 + s2 >= 84) and (step == 3): return 1
    elif (s1 + s2 < 84 and step == 3) or\
        (s1 + s2 >= 84 and step < 3): return 0
    return f(s1 + 1, s2, step + 1) or f(s1, s2 + 1, step + 1) or\
        f(s1*2, s2, step + 1) or f(s1, s2*3, step + 1)

print('zadazha 19')
for s2 in range(1, 68):
    if f(16, s2):
        print(s2)
        break



def f(s1, s2, step=1): # 1p 2v 3p 4v 5p 6v
    if (s1 + s2 >= 84) and (step == 4): return 1
    elif (s1 + s2 < 84 and step == 4) or\
        (s1 + s2 >= 84 and step < 4): return 0

    if step%2:
        return f(s1 + 1, s2, step + 1) or f(s1, s2 + 1, step + 1) or\
            f(s1*2, s2, step + 1) or f(s1, s2*3, step + 1)
    return f(s1 + 1, s2, step + 1) and f(s1, s2 + 1, step + 1) and\
            f(s1*2, s2, step + 1) and f(s1, s2*3, step + 1)
    

print('zadazha 20')
for s2 in range(1, 68):
    if f(16, s2):
        print(s2)
        


# step == 3 or step == 5   <=======> step in (3, 5)
        

def f(s1, s2, step=1): # 1p 2v 3p 4v 5p 6v proverka na 3 / 5
    if (s1 + s2 >= 84) and (step in (3, 5)): return 1
    elif (s1 + s2 < 84 and step == 5) or\
        (s1 + s2 >= 84 and step < 5): return 0

    if step%2: 
        return f(s1 + 1, s2, step + 1) and f(s1, s2 + 1, step + 1) and\
            f(s1*2, s2, step + 1) and f(s1, s2*3, step + 1)
    return f(s1 + 1, s2, step + 1) or f(s1, s2 + 1, step + 1) or\
            f(s1*2, s2, step + 1) or f(s1, s2*3, step + 1)
    

print('zadazha 21')
for s2 in range(1, 68):
    if f(16, s2):
        print(s2)

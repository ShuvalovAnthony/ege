# def f19(s, step=1): # 1p 2v 3p 4v 5p
#     if (s >= 129) and (step == 3): return 1
#     elif (s >= 129): return 0

#     if step%2:
#         return f19(s + 1, step + 1) and \
#         f19(s*2, step + 1)
    
#     return f19(s + 1, step + 1) or \
#         f19(s*2, step + 1)


# for s in range(1, 129):
#     if f19(s):
#         print(s)



# def f20(s, step=1): # 1p 2v 3p 4v 5p
#     if (s >= 129) and (step == 4): return 1
#     elif (s >= 129): return 0

#     if step%2 == 0:
#         return f20(s + 1, step + 1) and \
#         f20(s*2, step + 1)
    
#     return f20(s + 1, step + 1) or \
#         f20(s*2, step + 1)


# for s in range(1, 129):
#     if f20(s):
#         print(s)


def f21(s, step=1): # 1p 2v 3p 4v 5p
    if (s >= 129) and (step in (3, 5)): return 1
    elif (s >= 129): return 0

    if step%2:
        return f21(s + 1, step + 1) and \
        f21(s*2, step + 1)
    
    return f21(s + 1, step + 1) or \
        f21(s*2, step + 1)


for s in range(1, 129):
    if f21(s):
        print(s)


# def f19(s1, s2, step=0): # 1p 2v 3p 4v 5p
#     if (s1*s2 >= 63) and (step == 2): return True
#     elif (s1*s2 >= 63) and (step != 2): return False


#     if step%2 == 1:
#         return f19(s1 + 1, s2, step + 1) and \
#         f19(s1*2, s2, step + 1) and \
#         f19(s1, s2 + 1, step + 1) and \
#         f19(s1, s2*2, step + 1)
    
#     return f19(s1 + 1, s2, step + 1) or \
#         f19(s1*2, s2, step + 1) or \
#         f19(s1, s2 + 1, step + 1) or \
#         f19(s1, s2*2, step + 1)

# print('19 ------')
# for s2 in range(1, 32):
#     if f19(2, s2):
#         print(s2)
#         break



# def f20(s1, s2, step=0): # 1p 2v 3p 4v 5p
#     if (s1*s2 >= 63) and (step == 3): return True
#     elif (s1*s2 >= 63): return False

#     if step%2 == 1:
#         return f20(s1 + 1, s2, step + 1) and \
#         f20(s1*2, s2, step + 1) and \
#         f20(s1, s2 + 1, step + 1) and \
#         f20(s1, s2*2, step + 1)
    
#     return f20(s1 + 1, s2, step + 1) or \
#         f20(s1*2, s2, step + 1) or \
#         f20(s1, s2 + 1, step + 1) or \
#         f20(s1, s2*2, step + 1)

# print('20 ------')
# for s2 in range(1, 32):
#     if f20(2, s2):
#         print(s2)

def f21(s1, s2, step=1): # 1p 2v 3p 4v 5p
    if (s1*s2 >= 63) and (step in (3, 5)):
        return step
    elif (
        (s1*s2 < 63) and (step == 5)
        ) or (s1*s2 >= 63): return 0

    if step%2:
        return f21(s1 + 1, s2, step + 1) and \
        f21(s1*2, s2, step + 1) and \
        f21(s1, s2 + 1, step + 1) and \
        f21(s1, s2*2, step + 1)
    
    return f21(s1 + 1, s2, step + 1) or \
        f21(s1*2, s2, step + 1) or \
        f21(s1, s2 + 1, step + 1) or \
        f21(s1, s2*2, step + 1)

print('21 ------')
for s2 in range(1, 32):
    if f21(2, s2):
        print(s2)
        
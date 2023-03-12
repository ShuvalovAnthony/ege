# results = []

# def f(s1, s2, start_s2=None, step=1): # 1p 2v 3p 4v 5p
#     if (s1 + s2 >= 107) and step == 3:
#         if (s1 + s2 <= 170):
#             results.append([start_s2, step%2])
#         else:
#             results.append([start_s2, (step + 1)%2])
#     elif ((s1 + s2 >= 107) or\
#           ((s1 + s2) < 107) and (step == 3)): return 0
    
#     return f(s1 + 10, s2, start_s2, step + 1) or\
#     f(s1*2, s2, start_s2, step + 1) or\
#     f(s1, s2 + 10, start_s2, step + 1) or\
#     f(s1, s2*2, start_s2, step + 1)


# for s2 in range(1, 101):
#     f(5, s2, s2)

# for i in results:
#     if i[1] == 1:
#         print(i)
#         break

results = []


def f(s1, s2, start_s2=None, step=1): # 1p 2v 3p 4v 5p
    if (s1 + s2 >= 107) and (step in (3, 4)):
        if (s1 + s2 <= 170):
            results.append([start_s2, step%2])
        else:
            results.append([start_s2, (step + 1)%2])
    elif ((s1 + s2 >= 107) or\
          ((s1 + s2) < 107) and (step == 3)): return 0
    
    return f(s1 + 10, s2, start_s2, step + 1) or\
    f(s1*2, s2, start_s2, step + 1) or\
    f(s1, s2 + 10, start_s2, step + 1) or\
    f(s1, s2*2, start_s2, step + 1)


for s2 in range(1, 101):
    f(5, s2, s2)

for i in results:
    if i[1] == 1:
        print(i)
        break
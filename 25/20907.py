def f(s1, s2, step=1): # 1p 2v 3p 4v 5p
    if (step == 3 and (s1 + s2 >= 81)): return True
    if (
        (step == 3 and (s1 + s2 < 81)) or
        (step < 3 and (s1 + s2 >= 81))
    ):
        return False
    

    moves = [
        f(s1 + 1, s2, step + 1),
        f(s1, s2 + 1, step + 1),
        f(s1*2, s2, step + 1),
        f(s1, s2*2, step + 1),
    ]

    if step%2 == 0:
        return any(moves)
    return any(moves)


for s2 in range(1, 74):
    if f(7, s2):
        print(s2)
        break



# def f(s1, s2, step=1): # 1p 2v 3p 4v 5p
#     if (step == 4 and (s1 + s2 >= 81)): return True
#     if (
#         (step == 4 and (s1 + s2 < 81)) or
#         (step < 4 and (s1 + s2 >= 81))
#     ):
#         return False
    

#     moves = [
#         f(s1 + 1, s2, step + 1),
#         f(s1, s2 + 1, step + 1),
#         f(s1*2, s2, step + 1),
#         f(s1, s2*2, step + 1),
#     ]

#     if step%2 == 0:
#         return all(moves)
#     return any(moves)


# for s2 in range(1, 74):
#     if f(7, s2):
#         print(s2)


# def f(s1, s2, step=1): # 1p 2v 3p 4v 5p
#     if (step in (3,) and (s1 + s2 >= 81)): return True
#     if (
#         (step == 3 and (s1 + s2 < 81)) or
#         (step < 3 and (s1 + s2 >= 81))
#     ):
#         return False
    

#     moves = [
#         f(s1 + 1, s2, step + 1),
#         f(s1, s2 + 1, step + 1),
#         f(s1*2, s2, step + 1),
#         f(s1, s2*2, step + 1),
#     ]

#     if step%2 == 0:
#         return any(moves)
#     return all(moves)


# for s2 in range(1, 74):
#     if f(7, s2):
#         print(s2)

# first = [15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77]
# second = [19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64]


# res = []

# for i in first:
#     if i not in second:
#         res.append(i)

# print(res)
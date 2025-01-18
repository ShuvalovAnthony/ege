# def f19(h1, h2, step=1): # 1p 2v 3p 4v 5p
#     if (h1 + h2 <= 72) and (step == 3):
#         return True
#     elif (
#         ((h1 + h2 > 72) and (step == 3)) or
#         ((h1 + h2 <= 72) and (step < 3))
#     ): return False

#     moves = [
#         f19(h1 - 3, h2, step + 1),
#         f19(h1//2 + h1%2, h2, step + 1),
#         f19(h1, h2 - 3, step + 1),
#         f19(h1, h2//2 + h2%2, step + 1),
#     ]

#     return any(moves)



# for s in range(400, 22, -1):
#     if f19(50, s):
#         print(s)



# def f20(h1, h2, step=1): # 1p 2v 3p 4v 5p
#     if (h1 + h2 <= 72) and (step == 4):
#         return True
#     elif (
#         ((h1 + h2 > 72) and (step == 4)) or
#         ((h1 + h2 <= 72) and (step < 4))
#     ): return False

#     moves = [
#         f20(h1 - 3, h2, step + 1),
#         f20(h1//2 + h1%2, h2, step + 1),
#         f20(h1, h2 - 3, step + 1),
#         f20(h1, h2//2 + h2%2, step + 1),
#     ]

#     if step%2: # p
#         return any(moves)
#     return all(moves)


# res = []
# for s in range(400, 22, -1):
#     if f20(50, s):
#         res.append(s)

# print(min(res), max(res))




def f21(h1, h2, step=1): # 1p 2v 3p 4v 5p
    if (h1 + h2 <= 72) and (step in (3, 5)):
        return True
    elif (
        ((h1 + h2 > 72) and (step == 5)) or
        ((h1 + h2 <= 72) and (step < 5))
    ): return False

    moves = [
        f21(h1 - 3, h2, step + 1),
        f21(h1//2 + h1%2, h2, step + 1),
        f21(h1, h2 - 3, step + 1),
        f21(h1, h2//2 + h2%2, step + 1),
    ]

    if step%2: # p
        return all(moves)
    return any(moves)



for s in range(400, 22, -1):
    if f21(50, s):
        print(s)


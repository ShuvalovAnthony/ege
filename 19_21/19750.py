# def f19(h, step=1): # 1p 2v 3p 4v 5p 6v
#     if (h <= 19) and (step == 3):
#         return True
#     elif (
#         ((h <= 19) and (step < 3)) or
#         ((h > 19) and (step == 3))
#     ):
#         return False
    
#     moves = [f19(h - 5, step + 1)]
#     if h%2 == 0: moves.append(f19(h//2, step + 1))
#     if h%3 == 0: moves.append(f19(h//3, step + 1))
#     if h%2 and h%3: moves.append(f19(h + 1, step + 1))

#     if step%2:
#         return all(moves)
    
#     return any(moves)

# for s in range(20, 200):
#     if f19(s):
#         print(s)
#         break


# def f20(h, step=1): # 1p 2v 3p 4v 5p 6v
#     if (h <= 19) and (step == 4):
#         return True
#     elif ((h <= 19) and (step == 2)): return 0
#     elif (
#         ((h <= 19) and (step < 4)) or
#         ((h > 19) and (step == 4))
#     ):
#         return False
    
#     moves = [f20(h - 5, step + 1)]
#     if (h%2 == 0): moves.append(f20(h//2, step + 1))
#     if (h%3 == 0): moves.append(f20(h//3, step + 1))
#     if (h%2 and h%3): moves.append(f20(h + 1, step + 1))

#     if step%2 == 0:
#         return all(moves)
    
#     if any(moves):
#         return moves

# res = []
# for s in range(20, 50):
#     f_res = f20(s)
#     if f_res:
#         print(f_res, s)

# print(sorted(res))





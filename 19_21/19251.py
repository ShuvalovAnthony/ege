# def f19(h, step=1): # h - heap куча 1p 2v 3p 4v 5p 6v
#     if (h >= 132) and (step == 3):
#         return True
#     elif (
#         ((h >= 132) and (step < 3)) or
#         ((h < 132) and (step == 3))
#     ): return False

#     moves = [f19(h + 3, step + 1),
#              f19(h + 6, step + 1),
#              f19(h*3, step + 1)]
    
#     if step%2 == 1: # 1 3 5 7...
#         return all(moves)
    
#     return any(moves)


# for s in range(1, 132):
#     if f19(s):
#         print(s)
#         break



# def f20(h, step=1): # h - heap куча 1p 2v 3p 4v 5p 6v
#     if (h >= 132) and (step == 4):
#         return True
#     elif (
#         ((h >= 132) and (step < 4)) or
#         ((h < 132) and (step == 4))
#     ): return False

#     moves = [f20(h + 3, step + 1),
#              f20(h + 6, step + 1),
#              f20(h*3, step + 1)]
    
#     if step%2 == 1: # 1 3 5 7...
#         return any(moves)
    
#     return all(moves)


# for s in range(1, 132):
#     if f20(s):
#         print(s)
    


# def f21(h, step=1): # h - heap куча 1p 2v 3p 4v 5p 6v
#     if (h >= 132) and (step in (3, 5)):
#         return True
#     elif (
#         ((h >= 132) and (step < 5)) or
#         ((h < 132) and (step == 5))
#     ): return False

#     moves = [f21(h + 3, step + 1),
#              f21(h + 6, step + 1),
#              f21(h*3, step + 1)]
    
#     if step%2 == 1: # 1 3 5 7...
#         return all(moves)
    
#     return any(moves)


# for s in range(1, 132):
#     if f21(s):
#         print(s)
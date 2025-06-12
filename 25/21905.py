# def f(s, step=1): # 1p 2v 3p 4v 5p
#     # Условие победы
#     if (step == 3) and (s >= 67): return True
#     # Условия поражения (набрали нужно кол-во слишком рано/
#     # не набрали нужное колво когда надо)
#     elif (
#         (step == 3 and s < 67) or
#         (step < 3 and s >= 67)
#     ):
#         return False
    
#     # Все ходы, не забываем писать f !!!!!!!!!
#     moves = [
#         f(s + 1, step + 1),
#         f(s + 4, step + 1),
#         f(s*3, step + 1)
#     ]


#     # Победитель ВСЕГДА any
#     # Проигравший all - если неважно какой ход
#     # Проигравший any - НЕУДАЧНый ход
#     if step%2 == 0: # Vanyas moves
#         return any(moves)
#     return all(moves)


# for s in range(1, 67):
#     if f(s):
#         print(s)



# def f(s, step=1): # 1p 2v 3p 4v 5p
#     # Условие победы
#     if (step == 4) and (s >= 67): return True
#     # Условия поражения (набрали нужно кол-во слишком рано/
#     # не набрали нужное колво когда надо)
#     elif (
#         (step == 4 and s < 67) or
#         (step < 4 and s >= 67)
#     ):
#         return False
    
#     # Все ходы, не забываем писать f !!!!!!!!!
#     moves = [
#         f(s + 1, step + 1),
#         f(s + 4, step + 1),
#         f(s*3, step + 1)
#     ]


#     # Победитель ВСЕГДА any
#     # Проигравший all - если неважно какой ход
#     # Проигравший any - НЕУДАЧНый ход
#     if step%2 == 0: # Vanyas moves
#         return all(moves)
#     return any(moves) # Petyas moves


# for s in range(1, 67):
#     if f(s):
#         print(s)






def f(s, step=1): # 1p 2v 3p 4v 5p
    # Условие победы
    if (step in (3,)) and (s >= 67): return True
    # Условия поражения (набрали нужно кол-во слишком рано/
    # не набрали нужное колво когда надо)
    elif (
        (step == 3 and s < 67) or
        (step < 3 and s >= 67)
    ):
        return False
    
    # Все ходы, не забываем писать f !!!!!!!!!
    moves = [
        f(s + 1, step + 1),
        f(s + 4, step + 1),
        f(s*3, step + 1)
    ]


    # Победитель ВСЕГДА any
    # Проигравший all - если неважно какой ход
    # Проигравший any - НЕУДАЧНый ход
    if step%2 == 0: # Vanyas moves
        return any(moves)
    return all(moves) # Petyas moves


for s in range(1, 67):
    if f(s):
        print(s)
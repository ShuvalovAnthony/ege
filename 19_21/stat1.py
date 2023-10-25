def f19(s, step=1): # 1p 2v 3p 4v 5p
    if (s >= 108) and (step == 3): return 1
    elif (s >= 108) or (s < 108 and step > 3): return 0


    moves_chet = [
        f19(s + 1, step + 1),
        f19(int(s * 1.5), step + 1)]
    moves_nechet = [
        f19(s + 1, step + 1),
        f19(s*2, step + 1)]

    if step%2:
        if s%2: return all(moves_nechet)
        else: return all(moves_chet)
    
    if s%2: return any(moves_nechet)
    else: return any(moves_chet)

print('задача 19')
for s in range(107, 0, -1):
    if f19(s):
        print(s)
        break


print('задача 20')
def f20(s, step=1): # 1p 2v 3p 4v 5p
    if (s >= 108) and (step == 4): return 1
    elif (s >= 108) or (s < 108 and step > 4): return 0


    moves_chet = [
        f20(s + 1, step + 1),
        f20(int(s * 1.5), step + 1)]
    moves_nechet = [
        f20(s + 1, step + 1),
        f20(s*2, step + 1)]

    if step%2 == 0:
        if s%2: return all(moves_nechet)
        else: return all(moves_chet)
    
    if s%2: return any(moves_nechet)
    else: return any(moves_chet)

res = []
for s in range(1, 108):
    if f20(s): res.append(s)

print(*res[:2])


print('задача 21')
def f21(s, step=1): # 1p 2v 3p 4v 5p
    if (s >= 108) and (step in (3, 5)): return 1
    elif (s >= 108) or (s < 108 and step > 5): return 0


    moves_chet = [
        f21(s + 1, step + 1),
        f21(int(s * 1.5), step + 1)]
    moves_nechet = [
        f21(s + 1, step + 1),
        f21(s*2, step + 1)]

    if step%2:
        if s%2: return all(moves_nechet)
        else: return all(moves_chet)
    
    if s%2: return any(moves_nechet)
    else: return any(moves_chet)


for s in range(107, 0, -1):
    if f21(s): 
        print(s)
        break


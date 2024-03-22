def f19(s, step=1):  # 1p 2v 3p 4v 5p
    if (s >= 103) and (step == 3):
        return True
    elif (
        ((s >= 103) and (step < 3)) or
        ((s < 103) and (step == 3)) or
        (s % 3 == 0)
    ):
        return False

    moves = []
    if (s + 1)%3 != 0: moves.append(f19(s + 1, step + 1))
    if (s + 2)%3 != 0: moves.append(f19(s + 2, step + 1))
    if (s * 2)%3 != 0: moves.append(f19(s * 2, step + 1))

    if step%2:
        return all(moves)

    return any(moves)



for s in range(1, 101 + 1):
    if f19(s):
        print(s)
        break

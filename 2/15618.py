# (x ∧ ¬y) ∨ (y ≡ z) ∨ ¬w

print('x', 'y', 'z', 'w')


for x in (0, 1):
    for y in (0, 1):
        for z in (0, 1):
            for w in (0, 1):
                if not ((x and (not y)) or (y == z) or (not w)):
                    print(x, y, z, w)


# 1-w   2-z  3-y 4-x
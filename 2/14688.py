# (x ∨ y) → (z ≡ x)

print('x', 'y', 'z')

for x in (0, 1):
    for y in (0, 1):
        for z in (0, 1):
            if not ((x or y) <= (z == x)):
                print(x, y, z)

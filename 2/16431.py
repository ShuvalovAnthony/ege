# ((y → x) ≡ (x → w)) ∧ (z ∨ x).

print('x', 'y', 'z', 'w')

for x in (0, 1):
    for y in (0, 1):
        for z in (0, 1):
            for w in (0, 1):
                if ((y <= x) == (x <= w)) and (z or x):
                    print(x, y, z, w)


#  1-y  2-w 3-x  4-z
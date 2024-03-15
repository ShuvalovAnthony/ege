from itertools import product, permutations

chet_8 = (0, 2, 4, 6) #("000", "010", "100", "110")
nechet_8 = (1, 3, 5) # ("001", "011", "101") "111" - не подходит


triplets = [bin(i)[2:].zfill(3) for i in range(7)]
bad_combos_10 = []
bad_combos_2 = []
for i in permutations(triplets, r=2):
    combo = "".join(i)
    if "111" in combo:
        bad_combos_2.append(combo)
        bad_combos_10.append(str(int(i[0], 2)) + str(int(i[1], 2)))


print(bad_combos_10)
print(bad_combos_2)


# 1
# 0 2 4 6
# 1 3 5    1 3 5   1 3 5
# for i in product("01234567", repeat=16):
#     ...

# print("DONE")
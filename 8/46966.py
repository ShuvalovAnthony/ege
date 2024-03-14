from itertools import permutations

combos = []

for g1 in 'ао':
    for g2 in 'ао':
        combos.append (g1 + g2)

for g1 in 'мрхс':
    for g2 in 'мрхс':
        combos.append (g1 + g2)
    
def check(word):
    for combo in combos:
        if combo in word: return False
    return True

res = set()
for word in permutations("росомаха", 8):
    word = "".join(word)
    if check(word): res.add(word)


print(len(res))


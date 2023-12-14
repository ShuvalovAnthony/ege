bad_combos = set()

for i in '02468':
    for j in '02468':
        bad_combos.add(i + j)

for i in '13579':
    for j in '13579':
        bad_combos.add(i + j)


def check(num):
    if len(set(num)) != 4: return False
    for i in bad_combos:
        if i in num: return False
    
    return True


counter = 0

for a1 in '123456789':
    for a2 in '0123456789':
        for a3 in '0123456789':
            for a4 in '0123456789':
                word = a1 + a2 + a3 + a4
                counter += check(word)


print(counter)
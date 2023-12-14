bad_combos = set()

for i in '0246':
    for j in '0246':
        bad_combos.add(i + j)

for i in '1357':
    for j in '1357':
        bad_combos.add(i + j)


def check(num):
    if len(set(num)) != 5: return False
    for i in bad_combos:
        if i in num: return False
    
    return True


counter = 0

for a1 in '234567':
    for a2 in '0234567':
        for a3 in '0234567':
            for a4 in '0234567':
                for a5 in '0234567':
                    word = a1 + a2 + a3 + a4 + a5
                    counter += check(word)


print(counter)
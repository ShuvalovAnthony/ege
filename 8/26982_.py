bad_combos = []

for i in '024680':
    for j in '024680':
        bad_combos.append(i + j)

for i in '13579':
    for j in '13579':
        bad_combos.append(i + j)


def check(word):
    for bad_word in bad_combos:
        if bad_word in word: return False
    return True

kolichestvo = 0

for a1 in '123456789':
    for a2 in '0123456789':
        for a3 in '0123456789':
            for a4 in '0123456789':
                for a5 in '0123456789':
                    for a6 in '0123456789':
                        word = a1 + a2 + a3 + a4 + a5 + a6
                        if (
                            (int(word)%5 == 0) and
                            check(word) and
                            (len(word) == len(set(word)))
                        ):
                            kolichestvo += 1

print(kolichestvo)
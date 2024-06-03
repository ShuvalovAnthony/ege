from itertools import product


def check(word: str):
    for i in "БНДРЛ":
        if (i + 'Е' in word) or ('Е' + i in word): return False
    return True


counter = 0
for word in product("БАНДЕРОЛЬ", repeat=7):
    word = "".join(word)

    if (word.count("Ь") <= 1) and check(word):
        counter += 1


print(counter)
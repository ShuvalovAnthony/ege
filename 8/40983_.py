from itertools import product


def check_1(word):
    if (
        word.count('г') == 2 and\
        word.count('е') == 1 and\
        word.count('о') == 1 and\
        word.count('р') == 1 and\
        word.count('и') == 1 and\
        word.count('й') == 1
    ): return True
    return False



words = set()

for word in product("георгий", repeat=7):
    word = ''.join(word)
    if check_1(word) and ('гг' not in word): words.add(word)

print(len(words))
from itertools import product

def check(word):
    counter = 0
    for i in range(4):
        if word[i] == "ВОЛК"[i]:
            counter += 1
    return counter == 2

counter = 0

for word in product("ПОЛЯКВ", repeat=4):
    word = ''.join(word)

    counter += check(word)

print(counter)
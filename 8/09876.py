from itertools import permutations


counter = 0

for word in permutations("КАБИНЕТ"):
    print(word)
    if word[-1] not in 'АИЕ':
        counter += 1

print(counter)
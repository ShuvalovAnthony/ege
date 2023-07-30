from itertools import permutations

words = set()

for word in permutations("георгий", 7):
    word = ''.join(word)
    if 'гг' not in word:
        words.add(word)


print(len(words))
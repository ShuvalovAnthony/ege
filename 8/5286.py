from itertools import permutations

words = set()

for i in permutations('АМФИБРАХИЙ', 10):
    word = ''.join(i)
    if (
        'ИИФАА' in word or
        'ААФИИ' in word
    ):
        words.add(word)

print(len(words))
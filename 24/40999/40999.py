f = open("24/40999/40999.txt").read()

words = f.split("E")

words_with_triple_a = []
for word in words:
    if words.count('A') >= 3:
        words_with_triple_a.append(word)

print(
    max([
        len(i) for i in words_with_triple_a
    ])
)
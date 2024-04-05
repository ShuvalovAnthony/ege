from itertools import product


index = 1
answer = 0

for word in product(
    sorted("ЭЗОТЕРИКА"), repeat=5
):
    if (
        (word[0] != "Т") and
        (word.count("А") <= 2) and
        (1 <= word.count("З") <= 2)
    ):
        answer = index
    index += 1

print(answer)
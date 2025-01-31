f = open("24/58491/58491.txt").read()

originals = ["ABC", "ACB", "BAC", "BCA", "CAB", "CBA"]

separators = []

for left in originals:
    for right in originals:
        if left[-1] == right[0]:
            res = left + right[1:]
            separators.append(res)
        if left[-2:] == right[:2]:
            res = left + right[-1]
            separators.append(res)

separators += originals

separators = sorted(separators, key=lambda x: len(x), reverse=True)


for sep in separators:
    f = f.replace(sep, " ")


print(
    max(
        [len(word) for word in f.split()]
    )
)
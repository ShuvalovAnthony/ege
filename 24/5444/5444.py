f = open("24/5444/24_5444.txt").read()


for i in range(30, 2, -1):
    for letter in "ABCDEF":
        f = f.replace(letter*i, '*'*i)


for i in "ABCDEF":
    f = f.replace(i, ' ')


print(
    max(
        [len(i)//3 for i in f.split()]
    ) * 3
)
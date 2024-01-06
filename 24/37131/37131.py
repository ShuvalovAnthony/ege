f = open("24/37131/24.txt").read()


f = f.replace("KL", " ").replace("LK", " ")

print(
    max(
        [len(i) for i in f.split()]
    ) + 2
)
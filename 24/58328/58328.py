from string import digits

f = open("24/58328/24_58328.txt").read()


for digit in digits:
    for i in range(30, 1, -1):
        f = f.replace(digit*i, " ")


print(
    max(
        [len(i) for i in f.split()]
    ) + 2
)

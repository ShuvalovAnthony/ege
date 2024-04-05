f = open("vars/dosrok2024/10/10_2.txt").read()



for symb in "!@#$%^&*().,-/?'|\"":
    f = f.replace(symb, " ")


counter = 0

for word in f.split():
    if (
        ("По" in word) or
        ("по" in word)
    ) and (len(word) > 2):
        print(word)
        counter += 1

print(counter)

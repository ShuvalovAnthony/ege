f = open("vars/dosrok2024/10/10.txt").read()



for symb in "!@#$%^&*().,-/?'|\"":
    f = f.replace(symb, " ")


counter = 0

for word in f.split():
    if word in ("Мой", "мой"):
        print(word)
        counter += 1

print(counter)

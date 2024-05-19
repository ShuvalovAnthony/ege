from fnmatch import fnmatch


f = open("10/61390/text.txt").read()


for i in "!@#$%^&*()><,.?»«":
    f = f.replace(i, '')

counter = 0
for word in f.split():
    if fnmatch(word, "*?тон?*"):
        counter += 1
        print(word)

print(counter)
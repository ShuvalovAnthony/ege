f = open("24/38602/24.txt").read()

f = f.replace("PP", " ")

words = f.split()

dlini = [len(i) for i in words]
max_dlina = max(dlini)

index_max_dlini = dlini.index(max_dlina)

max_word = words[index_max_dlini]

print(max_word)
print(len(max_word) + 2)
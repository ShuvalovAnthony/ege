# # Способ 1

f = open('24/27695/zadanie24_2.txt').read()

counter = 1
max_dlina = 0


for i in range(len(f) - 1):
    if f[i + 1] != f[i]:
        counter += 1
    else:
        max_dlina = max(max_dlina, counter)
        counter = 1


# print(max_dlina)



# # Способ 2

f = open('24/27695/zadanie24_2.txt').read()



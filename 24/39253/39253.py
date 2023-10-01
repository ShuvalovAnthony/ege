f = open('24/39253/24.txt').read()


dlini = [len(i) for i in f.split('D')]

max_dlina = 0

for i in range(len(dlini) - 1):
    max_dlina = max(
        max_dlina,
        dlini[i] + dlini[i + 1] + 1
    )

print(max_dlina)
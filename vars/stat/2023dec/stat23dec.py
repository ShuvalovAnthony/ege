# 24

f = open("vars/stat/2023dec/24.txt").read()

f = (f
     .replace("A", " ")
     .replace("B", " "))

indexes = [i for i in range(len(f)) if f[i] == " "]

# ----4----8--10----15---18
# stop - start + 1

max_len = 0

for i in range(len(indexes) - 3):
    max_len = max(max_len, indexes[i + 3] - indexes[i] + 1)

print(max_len)
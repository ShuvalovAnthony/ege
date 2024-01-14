f = open('27/28130/28130_A.txt')
# ????
f.readline()

nums_l = []
nums_g = []

for i in f:
    n = int(i)
    if n <= 50: nums_l.append(n)
    else: nums_g.append(n)


print(nums_g, nums_l)
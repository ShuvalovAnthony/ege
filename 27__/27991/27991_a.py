f = open('ege/27__/27991/27991_A.txt')

n = f.readline()


nums = []

for i in f:
    nums.append(int(i))

nums = set(nums)

max_sum = -1
answ = (0, 0)

for i in nums:
    for j in nums:
        if (i != j) and (abs(i - j)%2 == 0) and (i%17 == 0 or j%17 == 0) and (i + j > max_sum):
            max_sum = i + j
            answ = (i, j)

print(sorted(answ, reverse=True))

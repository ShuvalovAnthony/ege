f = open('27__/6320/27A.txt')

n, m = map(int, f.readline().split())

nums = [int(i) for i in f]
nums = nums[-m::] + nums + nums[:m]

max_summa = 0

for post in range(n):
    tmp_summa = 0
    for j in range(post, post + 2*m + 1): tmp_summa += nums[j]
    max_summa = max(max_summa, tmp_summa)

print(max_summa)
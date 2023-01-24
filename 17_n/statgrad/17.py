f = open('17/statgrad/17.txt')

nums = []

min_num_zak_na_5 = -1

for i in f:
    num = int(i)
    if num%10 == 5: # заканчивается на 5
        min_num_zak_na_5 = min(min_num_zak_na_5, num)
    nums.append(num)

kvadrat = min_num_zak_na_5**2


counter = 0
max_summa_kv = 0

for i in range(len(nums) - 1):
    for j in range(i + 1, i + 2):
        min_iz_pari = min(nums[i], nums[j])
        if (min_iz_pari%10 == 5) and \
            ((nums[i]**2 + nums[j]**2) < kvadrat):
            counter += 1
            max_summa_kv = max(max_summa_kv, (nums[i]**2 + nums[j]**2))


print(counter, max_summa_kv)

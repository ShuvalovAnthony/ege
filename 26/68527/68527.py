f = open("ege/26/68527/1_26.txt")

n = int(f.readline())

nums = sorted([int(i) for i in f], reverse=True)

max_kolvo_korzhei = 1
last_korzh = nums[0]

for num in nums[1:]:
    if num <= last_korzh - 4:
        max_kolvo_korzhei += 1
        last_korzh = num


print(max_kolvo_korzhei, last_korzh)
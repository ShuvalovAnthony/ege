f = open("27__/27891/27-B_2.txt")

nums = sorted([int(i) for i in f], reverse=True)

naib_krat = 0

for i in nums:
    if i%14 == 0:
        naib_krat = i
        break

print(naib_krat*nums[0])
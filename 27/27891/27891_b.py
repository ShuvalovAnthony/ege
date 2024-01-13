f = open("27/27891/27-B_2.txt")

nums = sorted([int(i) for i in f], reverse=True)

naib_krat = 0

for num in nums:
    if num%14 == 0:
        naib_krat = num
        break

print(naib_krat*nums[0])


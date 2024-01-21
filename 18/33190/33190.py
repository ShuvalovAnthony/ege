f = open("18/33190/33190.txt")


nums = [float(i.replace(",", ".")) for i in f]


podhod_posled = []

temp_posled = []

for i in range(len(nums) - 1):
    if abs(nums[i + 1] - nums[i]) <= 10:
        temp_posled.append(nums[i])
    else:
        temp_posled.append(nums[i])
        podhod_posled.append(temp_posled)
        temp_posled = []

#  [-14.19, -4.42, 5.21, 14.08, 19.64, 18.23, 8.47, -1.3, 6.42, 0.13, 9.88
def max_summa_podposled(posled):
    res = 0
    for i in range(len(posled)):
        for j in range(i + 1, len(posled) + 1):
            sub_posled = posled[i:j]
            res = max(res, sum(sub_posled))
    return int(res)


max_summa = 0

for posled in podhod_posled:
    max_summa = max(
        max_summa,
        max_summa_podposled(posled)
    )

print(max_summa)
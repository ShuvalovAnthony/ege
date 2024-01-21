f = open("18/33097/33097.txt")


nums = [float(i.replace(",", ".")) for i in f]


vse_summi = []

temp_summa = 0

for i in range(len(nums) - 1):
    if nums[i + 1] > nums[i]:
        temp_summa += nums[i]
    else:
        temp_summa += nums[i]
        vse_summi.append(int(temp_summa))
        temp_summa = 0


print(max(vse_summi))


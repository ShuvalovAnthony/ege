f = open('17/6353/17_6353.txt')


nums = [int(i) for i in f]

# макс элемент кратный 118 но не оканчивающийся на 8

max_na_8 = -10001

for i in nums:
    if (
        i%118 == 0 and
        i%10 != 8 # str(i)[-1] == '8'
    ):
        max_na_8 = max(max_na_8, i)


def check(num1, num2, num3):
    # хотя бы 1 делится на 118
    if ((num1%118 == 0) or
        (num2%118 == 0) or
        (num3%118 == 0)):
    # хотя бы 1 оканчивается на 118
        if ((num1%1000 == 118) or
            (num2%1000 == 118) or
            (num3%1000 == 118)):

            if (num1 + num2 + num3) > max_na_8:
                return True
    
    return False


counter = 0
kv_max_summi = -1


for i in range(len(nums) - 3):
    for j in range(i + 1, i + 2):
        for k in range(i + 2, i + 3):
            if check(nums[i], nums[j], nums[k]):
                counter += 1
                kv_max_summi = max(
                    kv_max_summi,
                    (nums[i] + nums[j] + nums[k])**2
                )


print(counter, kv_max_summi)
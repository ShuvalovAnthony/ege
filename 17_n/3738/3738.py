f = open('17_n/3738/17_3738.txt')


nums = [int(i) for i in f]

d = {i:0 for i in range(50)}


def check(num1, num2):
    summa_cifr_1 = 0
    for i in str(num1): summa_cifr_1 += int(i)
    summa_cifr_2 = 0
    for i in str(num2): summa_cifr_2 += int(i)

    return (summa_cifr_1, summa_cifr_2)


def summa_razryadov(num1, num2): # 123, 5678
    num1, num2 = str(num1), str(num2) # '123', '5678'
    perenos = False
    for i in range(-1, -6, -1): # -1 - посл цифра, -2 - предпоследняя
        try: # 7 8 - 15
            summa_razryadov = int(num1[i]) + int(num2[i])

            if perenos: d[summa_razryadov + 1] += 1
            else: d[summa_razryadov] += 1

            if summa_razryadov >= 10: perenos = True
            else: perenos = False
        except:
            break

counter = 0

for i in range(1, len(nums) - 1):
    summa_1, summa_2 = check(nums[i - 1], nums[i + 1])
    if summa_1 == summa_2:
        counter += 1
        summa_cifr_chisla_i = 0
        for i in str(nums[i]): summa_cifr_chisla_i += int(i)
        d[summa_cifr_chisla_i] += 1

new_d = {value: key for key, value in d.items()}

print('Разряды', max(new_d), new_d[max(new_d)])
print('Каунтер', counter)

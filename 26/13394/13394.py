import math

f = open("26/13394/26.6_13394.txt")

n = int(f.readline())

total = 0
nums = []

for i in f:
    n = int(i)
    if n <= 350:
        total += n
    else:
        nums.append(n)

nums = sorted(nums)

totalWinCustomer = total
totalWinShop = total

# лучший вариант покупателя - чеки по 3 ближайших
for i in range(0, len(nums), 3):
    subTotal = math.ceil(nums[i]*0.25 + nums[i + 1] + nums[i + 2])
    totalWinCustomer += subTotal

# лучший вариант магазина - общий чек
index = len(nums)//3 # - срез первой трети самых дешевых товаров
totalWinShop += math.ceil(sum(nums[:index])*0.25) + sum(nums[index:])

print(totalWinCustomer, totalWinShop)


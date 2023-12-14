f = open("17/37355/17.txt")

# одномерный массив (в списке 1 строка = 1 число)
nums = [int(i) for i in f] 


counter = 0
max_summa = -1

for i in range(len(nums) - 1):
    for j in range(i + 1, len(nums)):
        if (nums[i] + nums[j])%7 == 0:
            counter += 1

            max_summa = max(max_summa, nums[i] + nums[j])


print(counter, max_summa)
f = open('9/27526/data.txt')

nums = []

for stroka in f:
    nums += [float(i) for i in stroka.split()]

max_temp_popolam = max(nums)/2

avg = sum(nums)/len(nums)
avg_popolam = 23.9/2

count = 0

for num in nums:
    if num < max_temp_popolam and num > avg_popolam:
        count += 1

print(count)
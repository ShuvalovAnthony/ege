f = open("ege/27/17619/27B_17619.txt")

n = int(f.readline())

nums = [int(i) for i in f]

sorted_nums = sorted(nums)

trashhold_count = 1000

trashhold_min = sorted_nums[trashhold_count - 1]
trashhold_max = sorted_nums[-trashhold_count]

final_data = []



for num in nums:
    if (num >= trashhold_max) or (num <= trashhold_min):
        print(num)
        final_data.append(num)
print(final_data)
# j + m - i - k
# j > 0 m > 0           i < 0   k < 0
# i   j   k   m

max_sum = 0

for i in range(len(final_data)):
    for j in range(i + 1, len(final_data)):
        for k in range(j + 1, len(final_data)):
            for m in range(k + 1, len(final_data)):
                max_sum = max(max_sum, 
                    final_data[j] - final_data[i] + final_data[m] - final_data[k])


print(max_sum)
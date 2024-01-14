f = open("27/38604/27_A.txt")

n = f.readline()

nums = [int(i) for i in f]

max_sum = 0
len_max_sum = 10**6

for i in range(len(nums) - 1):
    for j in range(i + 1, len(nums) + 1):
        temp_list = nums[i:j]
        temp_sum = sum(temp_list)
        if (temp_sum%43 == 0) and (temp_sum >= max_sum):
            if temp_sum == max_sum:
                len_max_sum = min(len_max_sum, len(temp_list))
            else:
                len_max_sum = len(temp_list)
            max_sum = temp_sum


print(len_max_sum)

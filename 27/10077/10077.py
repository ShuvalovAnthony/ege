f = open("27/10077/27A_10077.txt")


k = int(f.readline())
nums = [int(i) for i in f]

dlini = []

for i in range(len(nums)):
    for j in range(i, len(nums)):
        len_temp_sum = j - i + 1
        diff_sum = sum(nums[:i]) + sum(nums[j + 1:])
        
        if (
            (diff_sum%k == 0) and 
            (diff_sum%len_temp_sum == 0) and
            (diff_sum > 0)
        ):
            dlini.append(len_temp_sum)


print(dlini)

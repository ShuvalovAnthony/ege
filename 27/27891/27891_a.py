f = open("27/27891/27-A_2.txt")

nums = [int(i) for i in f]

max_num = -1

for i in range(len(nums) - 1):
    for j in range(i + 1, len(nums)):
        proizved = nums[i]*nums[j]
        if proizved%14 == 0:
            max_num = max(max_num, proizved)


print(max_num)
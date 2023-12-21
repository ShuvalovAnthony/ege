# # file - B
# f = open("27/probnik23dec/27-B_12257.txt")

# nums_len = int(f.readline())
# nums = [int(i) for i in f]
# lefts = [0 for i in range(nums_len)]


# count = 0
# sumi = 0

# for i in range(1, len(nums)):
#     num = nums[i]
#     sumi += num

#     if sumi % 113 == 0:
#         count = count + 1
    
#     count += lefts[sumi % 113]
#     lefts[sumi % 113] += 1


# print(count)








# file - A
# f = open("27/probnik23dec/27-A_12257.txt")

# nums_len = f.readline()
# nums = [int(i) for i in f]


# max_len = 0

# for i in range(len(nums)):
#     for j in range(i + 1, len(nums)):
#         # i = 5
#         # j = 10
#         # 5 6 - 3

#         if sum(nums[i: j])%113 == 0:
#             max_len = max(max_len, j - i)

# print(max_len)
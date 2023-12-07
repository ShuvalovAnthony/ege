# f = open("27/59732/1_27_A.txt")

# diff = int(f.readline())
# n = int(f.readline())

# nums = [int(i) for i in f]

# reversed_nums = nums[::-1]


# print(sorted(nums)[-10::], "diff=", diff)


# print(
#     nums.index(804),
#     reversed_nums.index(804),
#     nums.index(803)
# )


print('-'*50)

f = open("27/59732/1_27_B.txt")

diff = int(f.readline())
n = int(f.readline())

nums = [int(i) for i in f]
reversed_nums = nums[::-1]


print(sorted(nums)[-10::], "diff=", diff)

ind_1 = nums.index(3571143)
ind_2 = reversed_nums.index(3571142)
ind_3 = reversed_nums.index(3571141)

print(
    ind_1,
    ind_2,
    ind_3
)


print(3571143 + 3571142 + 3571141)
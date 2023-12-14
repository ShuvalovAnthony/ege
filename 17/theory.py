f = open("relative_path_to_file")

# одномерный массив (в списке 1 строка = 1 число)
nums = [int(i) for i in f] 

# в списке 1 строка несколько
nums = [
    [int(i) for i in row.split()] for row in f
]


# 2 различных элемента последовательности

for i in range(len(nums) - 1):
    for j in range(i + 1, len(nums)):
        left_num = nums[i]
        right_num =nums[j]


# 2 соседних элемента
# 1 способ

for i in range(len(nums) - 1):
    left_num = nums[i]
    right_num =nums[i + 1]

# 2 способ
for i in range(len(nums) - 1):
    for j in range(i + 1, i + 2):
        left_num = nums[i]
        right_num =nums[j]


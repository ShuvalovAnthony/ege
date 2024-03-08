f = open("27/57434/1_27_B.txt")

k = int(f.readline())
n = int(f.readline())

nums = [int(i) for i in f]


nums_with_indexes = sorted(
    [
        [i, nums[i]] for i in range(len(nums))
    ],
    key=lambda x: x[1]
)

print(k)
print(nums_with_indexes[-10:])

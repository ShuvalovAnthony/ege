f = open('9/6898/6898.txt')

nums_list = [list(map(int, i.split())) for i in f]

counter = 0

for nums in nums_list:
    nums = sorted(nums)
    if (
        (nums[-1] < sum(nums[:-1])) and 
        ((nums[0] + nums[-1]) == (nums[1] + nums[2]))
    ):
        counter += 1

print(counter)
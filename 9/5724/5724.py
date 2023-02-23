'''
Например, последовательность глубин 10 5 2 20 30 считается холмом. Последовательности
 10 2 5 20 30 и 10 8 4 1 15 тоже считаются холмом. 1 2 3 4 5 это не холм
 '''
f = open('9/5724/5724.txt')

nums = list(map(int, i.split()) for i in f)

counter = 0

def check(nums):
    v_goru = True
    nums = list(nums)
    if (nums.index(min(nums)) in (0, 4)): return False

    for i in range(len(nums) - 1):
        if (nums[i + 1] < nums[i]):
            if v_goru:
                pass
            else:
                return False
        else:
            v_goru = False

    return True


for i in nums:
    if check(i): counter += 1

print(counter)


# check sposob 2

def check(nums:list):
    nums = list(nums)
    index_min = nums.index(min(nums))

    if index_min in (0, 4): return False

    for i in range(index_min - 1):
        if (nums[i + 1] >= nums[i]):
            return False

    for i in range(index_min, 4):
        if (nums[i + 1] <= nums[i]):
            return False

    return True
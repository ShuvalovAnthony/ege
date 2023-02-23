f = open('9/5917/5917.txt')

nums = [sorted(map(int, i.split())) for i in f]

count = 0

def check(nums: list):
    return nums[2]**2 < (nums[0] * nums[-1])
    
for i in nums:
    if (len(set(i)) == len(i)) and (check(i)):
        count += 1

print(count)
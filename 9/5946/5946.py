f = open('9/5946/5946.txt')

nums = [list(map(int, i.split())) for i in f]

counter = 0

def check(nums:list):
    chet_count = 0
    for i in nums:
        if i%2 == 0: chet_count += 1
    return chet_count > 3

for i in nums: # i - список чисел list
    if (len(set(i)) == len(i)) and (check(i)):
        counter += 1


print(counter)
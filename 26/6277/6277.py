# неявное условие!!!

f = open('26/6277/26_6277.txt')

n, free_space = map(int, f.readline().split())
nums = [int(i) for i in f]

# n, free_space = 6, 100
# nums = [30, 10, 40, 50, 10, 20]

cache = []

# первое заполнение кэша

for num in nums:
    if num <= free_space:
        free_space -= num
        cache.append(num)
    else: break

print(free_space, len(cache))

nums = nums[len(cache)::]

for i in range(len(nums)):
    flag = True
    cache = sorted(cache, reverse=True)
    while flag:
        if nums[i] <= max(cache) + free_space:
            flag = False
            for j in range(len(cache)):
                if nums[i] <= cache[j] + free_space:
                    free_space = free_space + cache[j] - nums[i]
                    cache[j] = nums[i]
                    break
        else:
            free_space += cache.pop(-1)
    
print(len(cache))

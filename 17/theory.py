f = open('file_name.txt', 'w') # 'w' - write, 'r' - read

f.readline() # - считать 1 строку


f = open('ege/17/37336/17.txt')

nums = []

for i in f:
    nums.append(int(i))

print(nums)
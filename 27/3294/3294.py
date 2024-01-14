f = open('27/3294/27-B.txt')

n = int(f.readline())
nums = [int(i) for i in f]



count = 0
for i in range(n):
    for j in range(i+6, n):
        if (nums[i] + nums[j])%2 and nums[i]*nums[j]%13 == 0:
            count += 1
    if i%100 == 0:
        print(i)




print(count)
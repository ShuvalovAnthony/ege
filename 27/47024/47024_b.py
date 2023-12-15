f = open("27/47024/27-B.txt")


nums = [int(i) for i in f]

lefts = [0 for i in range(1111)]


count = 0
sumi = 0


for i in range(1, len(nums)):
    num = nums[i]
    sumi += num

    if sumi % 1111 == 0:
        count = count + 1
    
    count += lefts[sumi % 1111]
    lefts[sumi % 1111] += 1


print(count)
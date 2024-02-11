f = open("17/40733/17.txt")

nums = [int(i) for i in f]

chetnie = []
for num in nums:
    if num%2 == 0: chetnie.append(num)

avg = sum(chetnie)/len(chetnie)

counter = 0
max_sum = 0

for i in range(len(nums) - 1): # nums[i] nums[i + 1]
    left = nums[i]
    right = nums[i + 1]

    if (
        ((left%3 == 0) or (right%3 == 0)) and
        ((left < avg) or (right < avg))
    ):
        counter += 1
        max_sum = max(max_sum, left + right)

print(counter, max_sum)
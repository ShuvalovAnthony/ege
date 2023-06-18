f = open('27__/3294/27-B.txt')

n = int(f.readline())
nums = [int(i) for i in f]


def count_pairs(arr, n):
    count = 0
    for i in range(n):
        for j in range(i+6, n):
            if (arr[i] + arr[j])%2 and arr[i]*arr[j]%13 == 0:
                count += 1
        if i%100 == 0:
            print(i)
    return count



print(count_pairs(nums, n))
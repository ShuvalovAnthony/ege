n = int(input())

matrix = []
for row in range(n):
    matrix.append([int(i) for i in input().split()])


def arifm_progr(nums: list):
    nums = sorted(nums)
    delta = nums[1] - nums[0]
    if not delta: return False
    for i in range(len(nums) - 1):
        if nums[i + 1] - nums[i] != delta:
            return False
    return True


def counter_right_diags(matrix):
    res = []
    n = len(matrix)
    
    for i in range(n - 1, -1, -1):
        diagonal = [matrix[j][j + i] for j in range(n - i)]
        if (
            (len(diagonal) not in (1, 2, n)) and
            arifm_progr(diagonal)
        ):
            res.append(diagonal)

    for i in range(1, n):
        diagonal = [matrix[i + j][j] for j in range(n - i)]
        if (
            (len(diagonal) not in (1, 2, n)) and
            arifm_progr(diagonal)
        ):
            res.append(diagonal)
    
    if len(res) >= 2: return res
    return False


answer = counter_right_diags(matrix)

if answer:
    print('Да')
    for row in answer:
        print(*row)
else:
    print('Нет')




'''
4
1 2 3 4
4 6 5 3
9 6 5 8
1 1 2 4

4
1 2 3 4
5 5 7 8
9 9 7 5
4 3 2 1
'''
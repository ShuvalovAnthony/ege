f = open("ege/26/stat2025/26.txt")

n = int(f.readline())


data = [[int(i) for i in row.split()] for row in f]

# data = [
#     [10, 1070],
#     [230, 1070],
#     [240, 1070],
#     [1070, 1400],
#     [1071, 1400]
#     ]

data = sorted(data, key=lambda x: (
    x[0],
    x[1]
))


def count_emp(minute):
    emps = 0
    for start, stop in data:
        emps += start <= minute <= stop
    return emps

max_len = 0
prelast_min_with_changes = 0
last_min_with_changes = 0

temp_len = 1
last_emp_count = count_emp(0)


for minute in range(1, 24*60):
    temp_emp_count = count_emp(minute)

    if temp_emp_count == last_emp_count:
        temp_len += 1
        print(temp_emp_count, minute)
    else:
        print('------')
        max_len = max(max_len, temp_len)
        temp_len = 1
        prelast_min_with_changes = last_min_with_changes
        last_min_with_changes = minute

    last_emp_count = temp_emp_count

print(max_len, prelast_min_with_changes)
    

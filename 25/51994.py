from fnmatch import fnmatch

for num in range(3123, 10**9 + 1, 3123):
    if fnmatch(str(num), "12*63?5?"):
        print(num)
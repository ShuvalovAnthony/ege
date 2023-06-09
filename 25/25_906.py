from fnmatch import fnmatch

for i in range(999, 10**9, 999):
    if fnmatch(str(i), '13???57?9'): print(i, i//999)
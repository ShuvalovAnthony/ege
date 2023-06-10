from fnmatch import fnmatch

for i in range(253, 10**8 + 1, 253):
    if fnmatch(str(i), "12??15*6"): print(i, i//253)
from fnmatch import fnmatch


for i in range(2031, 10**9 + 1, 2031):
    if fnmatch(
        str(i), '*31*65'
    ) and i%31 == 0:
        print(i, i//2031)
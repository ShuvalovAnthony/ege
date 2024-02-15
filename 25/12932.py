from fnmatch import fnmatch


for num in range(2024, 10**10 + 1, 2024):
    if fnmatch(str(num), "1?2*4") and (int(num**0.5) == num**0.5):
        print(num, num//2024)




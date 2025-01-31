from fnmatch import fnmatch


# def check(num):
#     num = str(num)
#     return (
#         (num[0] == "3") and
#         (num[2:4] == "12") and
#         (num[5:7] == "14") and
#         (num[-1] == "5")
#     )


for num in range(1917, 10**10 + 1, 1917):
    if fnmatch(str(num), "3?12?14*5"):
        print(num, num//1917)
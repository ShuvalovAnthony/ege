# 1?2139*4

# 1 s1 2139 s2 4
# 1?2 139 __4
# 999 999 999



# for s1 in '0123456789': # str
#     for s2 in range(10**2): # int
#         res = int('1' + s1 + '2139' + str(s2) + '4')
#         if res%2023 == 0:
#             print(res, res//2023)

# for i in range(162139404, 10**10 + 1, 2023):
#     s = str(i)
#     if s[0] == '1' and s[2:6] == '2139' and s[-1] == '4':
#         print(i, i//2023)










def mask(n: int): # проверяем маску
    s = str(n)
    if s[0] == '1' and s[2:6] == '2139' and\
        s[-1] == '4': return True
    return False


for i in range(2023, 10**10, 2023): # START!!!! STEP!!!!!!
    if mask(i) and i%2023 == 0:
        print(i, i//2023)

    
for i in '0123456789':
    for j in '0123456789':
        num = int('12345' + i + '7' + j + '8')
        if num%23 == 0:
            print(num)
            break


# def mask(num: str):
#     # 12345?7?8
#     num = str(num)
#     if num[:5] == '12345' and num[-1] == '8' \
#         and num[-3] == '7':
#         return True
#     return False



# for i in range(123451718, 10**9, 23):
#     if mask(i): print(i, i//23)
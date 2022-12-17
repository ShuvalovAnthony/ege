# import string

# print(string.ascii_uppercase)




for x in '0123456789ABCDEFGHI':
    num_1 = int('321' + x + '4', 19)
    num_2 = int('498' + x + '9', 19)
    if (num_1 + num_2)%23 == 0:
        print((num_1 + num_2)//23)
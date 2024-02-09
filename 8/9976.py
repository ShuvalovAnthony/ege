# from itertools import product
# from string import digits


# alph = digits + 'AB'

# def prime(letter: str):
#     return letter in '012357B'


# def check(s: str):
#     prime_count = 0
#     for letter in s: prime_count += prime(letter)

#     return (
#         (prime_count >= 2) and
#         (int(s[0], 12)%2 != int(s[-1], 12)%2)
#     )


# res = {i:0 for i in range(3, 9)}


# # for i in range(3, 7):
# #     temp_counter = 0
# #     for s in product(alph, repeat=i):
# #         temp_counter += check(''.join(s))
    
# #     res[i] = temp_counter

# res = {3: 548, 4: 8508, 5: 113716, 6: 1432492, 7: 0, 8: 0}

# print(res)

# for i in res:
#     try:
#         print(res[i], res[i + 1], res[i + 2]* 5/(res[i + 1] + res[i]))
#     except:
#         ...


# n = int(input())


# def deliteli(num: int):
#     deliteli = set()
#     for i in range(1, int(num**0.5) + 1, 2):
#         if num % i == 0:
#             deliteli.add(i)
#             if ((num//i)**0.5 == int((num//i)**0.5)):
#                 return [num//i]
#     return deliteli


# def max_square_div(deliteli: list):
#     for delitel in sorted(deliteli, reverse=True):
#         if (delitel**0.5 == int(delitel**0.5)):
#             return delitel


# print(
#     max_square_div(
#         deliteli(n)
#     )
# )



# for i in range(10**18 - 1, 10**7, -2):
#     print(i, max_square_div(deliteli(i)))


# def factors(n):
#     return set(x for tup in ([i, n//i] 
#                 for i in range(1, int(n**0.5)+1) if n % i == 0) for x in tup if (x**0.5 == int(x**0.5)))


# print(factors(999999998000000001))



# sposob 1

# def not_trivial_delit(n:int):
#     deliteli = []
#     for i in range(2, int(n**0.5) + 1):
#         if n%i == 0:
#             deliteli += [i, n//i]
#     return sorted(set(deliteli))


# counter = 5

# for i in range(3*10**8 + 1, 3*10**12):
#     if (len(not_trivial_delit(i)) >= 5):
#         print(not_trivial_delit(i)[-5])
#         counter -= 1
#     if not counter: break



# sposob 2

# def not_trivial_delit(n:int):
#     max_deliteli = []
#     min_deliteli = []
#     for i in range(2, int(n**0.5) + 1):
#         if n%i == 0:
#             min_deliteli.append(i)
#             max_deliteli.append(n//i)
#         if len(max_deliteli) >= 5:
#             return max_deliteli[-1]
#     if (len(max_deliteli) + len(min_deliteli)) > 5:
#         result = min_deliteli + max_deliteli[::-1]
#         return result[-5]
#     return False


# counter = 5

# for i in range(3*10**8 + 1, 3*10**12):
#     if not_trivial_delit(i):
#         print(not_trivial_delit(i))
#         counter -= 1
#     if not counter: break









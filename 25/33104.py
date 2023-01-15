def delit(n: int):
    if n**0.5 != int(n**0.5):
        return False
    deliteli = []
    for i in range(2, int(n**0.5) - 1):
        if n%i == 0:
            deliteli.append(i)
            deliteli.append(n//i)
        if len(deliteli) > 2:
            return False
    if len(deliteli) == 2:
        return deliteli[-1]
    return False
        

for i in range(289123456, 389123456):
    if delit(i): print(i, delit(i))


# Лучший способ


# def simple(n):
#     for i in range(2, int(n**0.5) + 1):
#         if n%i == 0:
#             return False
#     return True



# def delit(n):
#     if n**0.25 == int(n**0.25):
#         return simple(n**0.25)
#     return False


# for i in range(289123456, 389123456):
#     if delit(i): print(i, delit(i))
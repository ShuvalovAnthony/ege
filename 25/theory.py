# является ли число простым
def prime(n:int):
    for i in range(2, int(n**0.5) + 1):
        if n%i == 0: return False
    return True


# ВСЕ (включая 1 и само число) делители числа
def all_delit(n:int):
    deliteli = []
    for i in range(1, int(n**0.5) + 1):
        if n%i == 0:
            deliteli += [i, n//i]
    return sorted(set(deliteli))


# все НЕТРИВИАЛЬНЫЕ (кроме 1 и самого числа) делители числа
def not_trivial_delit(n:int):
    deliteli = []
    for i in range(2, int(n**0.5) + 1):
        if n%i == 0:
            deliteli += [i, n//i]
    return sorted(set(deliteli))


def not_trivial_delit_2(n: int):
    return all_delit(n)[1:-1]


# все простые множители числа
def prime_mnozh(n:int):
    prime_delit = []
    for delitel in all_delit(n):
        if prime(delitel): prime_delit.append(delitel)
    return prime_delit


# разложение на простые множители
def razlozh_na_prostie(n:int):
    prostie = prime_mnozh(n)[1::]
    mnozh = {i: 0 for i in prostie}
    for i in prostie:
        while (n%i == 0):
            n //= i
            mnozh[i] += 1
    result = ''
    for key, value in mnozh.items():
        result += str(key) + '^' + str(value) + ' * '
    return result


# разложение на простые множители
def kolvo_prost_mnpzh(n:int):
    prostie = prime_mnozh(n)[1::]
    count = 0
    for i in prostie:
        while (n%i == 0):
            n //= i
            count += 1  
    return count





# # все делите числа
# # тривиальные делители - это 1 и само число
# def deliteli(num):
#     deliteli = set()

#     for i in range(1, int(num**0.5) + 1): 
#         if num%i == 0:
#             deliteli.add(i)
#             deliteli.add(num//i)

#     return sorted(list(deliteli))

# print(len(deliteli(18385428600)))


# def notTriviaDeliteli(num):
#     deliteli = set()

#     for i in range(2, int(num**0.5)): 
#         if num%i == 0:
#             deliteli.add(i)
#             deliteli.add(num//i)

#     return sorted(list(deliteli))

# print(notTriviaDeliteli(100))



# # функция, которая проверяет, что у числа 9 нетривиальных делителей

# def check(num):
#     deliteli = set()

#     for i in range(2, int(num**0.5)):
#         if num%i == 0:
#             deliteli.add(i)
#             deliteli.add(num//i)
        
#         # if len(deliteli) > 9: return False

#     if len(deliteli) == 9:
#         return deliteli


# print(check(100))


# def prime(num):
#     for i in range(2, int(num**0.5) + 1):
#         if num%i == 0: return False
#     return True
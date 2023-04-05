def num_delit(n:int):
    deliteli = []
    for i in range(1, int(n**0.5) + 1):
        if n%i == 0:
            deliteli += [i, n//i]
    return len(set(deliteli))


# вариант функции 2
# def num_delit(n:int):
#     counter = int(n**0.5) == n**0.5
#     for i in range(1, int(n**0.5) + 1):
#         if n%i == 0: counter += 2
#     return counter


max_num_od_dividers = 0
answer_num = 0


for i in range(568023, 569230 + 1):
    if num_delit(i) > max_num_od_dividers:
        max_num_od_dividers = num_delit(i)
        answer_num = i


print(max_num_od_dividers, answer_num)
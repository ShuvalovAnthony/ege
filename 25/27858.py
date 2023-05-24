def delit(num):
    counter = 0
    for i in range(1, num + 1):
        if num%i == 0:
            counter += 1
    return counter



max_kol_delit = 0
max_number = 0


for num in range(120115, 120200 + 1):
    if delit(num) >= max_kol_delit:
        max_kol_delit = delit(num)
        max_number = num


print(max_kol_delit, max_number)
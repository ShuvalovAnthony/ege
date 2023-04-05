# slow!!
def chet_delit(n):
    deliteli = []
    for i in range(2, n + 1):
        if n%i == 0 and i%2 == 0:
            deliteli.append(i)
            if len(deliteli) > 4: return False

    if len(deliteli) == 4: return deliteli
    return False


for i in range(101000000, 102000000):
    if chet_delit(i): print(chet_delit(i), i)



# 102//2 = 51
# 102//6 = 17
# 102//34 = 3
# 102//102 = 1


# 110//2 == 55
# 110//10 = 11
# 110//22 = 5
# 110//110 = 1  
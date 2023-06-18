f = open("27__/47231/27_B.txt")


def conts(np, pp=36):
    """np - колво пробирок, pp - пробирок в контейнере"""
    return np//pp + 1*bool(np%pp)

labs = []
cont_count = 0
current_summa = 0

for i in f:
    coord, prob = map(int, i.split())
    cont = conts(prob)
    labs.append((coord, cont))
    current_summa += (coord - 1)*cont # 1 - координата первого центра ИЗ ФАЙЛА
    cont_count += cont



cont_l = 0
cont_r = cont_count - 3 # 3 - колво контейнеров в первом пункте из файла

min_sum = 10**20

for i in range(len(labs) - 1):
    step = labs[i + 1][0] - labs[i][0] # след координата минус текущая
    cont_l += labs[i][1] # увеличиваем контейнеры слева
    current_summa += (cont_l*step - cont_r*step) # изменение в цене
    cont_r -= labs[i + 1][1] # пересчет конт справа
    min_sum = min(min_sum, current_summa)


print(min_sum)
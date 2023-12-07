def f(start, stop):
    if start == stop: return 1
    # здесь в or пишем все пункты, которые ИЗБЕГАЕМ
    elif (start > stop) or (start == 31): return 0
    # здесь пишем все действия автомата
    return f(start + 1, stop) + f(start*2, stop)

# 15 - обязательный пункт
print(f(2, 15)*f(15, 35))
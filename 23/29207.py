def f(start, stop): # содержит 11 и НЕ содержит 12
    if start == stop: return 1
    elif start > stop or start == 12: return 0
    return f(start+1, stop) + f(start*2,stop)

def f1(start, stop):# содержит 12 и НЕ содержит 11
    if start == stop:return 1
    elif start > stop or start == 11: return 0
    return f1(start+1, stop) + f1(start*2,stop)

print(
    f(2,11)*f(11,24) +
    f1(2,12)*f1(12,24)
    )
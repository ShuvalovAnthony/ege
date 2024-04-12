# for n in range(2, 123123):
#     bin_n = bin(n)[2:]
#     if n%2 == 0:
#         bin_n = bin_n[:-1]
#     else:
#         bin_n = '1' + bin_n
#         bin_n += bin(int(bin_n[-1]) + int(bin_n[-2]))[2:]
    
#     r = int(bin_n, 2)

#     if r == 202:
#         print(n)

results = []

def to3(num: int):
    digits = ''
    while num > 0:
        digits += str(num%3)
        num //= 3
    return digits[::-1]


def calculateSumCifr(num: int|str):
    num = str(num)
    return sum([int(i) for i in num])


for n in range(1, 10**4):
    tri_n = to3(n)
    sumCifr = calculateSumCifr(tri_n)
    if sumCifr%2 == 0:
        tri_n += to3(sumCifr)
    else:
        tri_n = '1' + tri_n + str(n%2)

    r = int(tri_n, 3)

    if r > 1105:
        results.append(r)

print(min(results))
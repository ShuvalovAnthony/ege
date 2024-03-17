def algo(n: int):
    bin_n = bin(n)[2:]
    if n%2 == 0: bin_n += '0'*bin_n.count('0')
    else: bin_n = '1'*bin_n.count('1') + bin_n
    return int(bin_n, 2)


for n in range(1000):
    if algo(n) > 2000:
        print(n)
        break
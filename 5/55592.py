
def kolvo_cifr(num):
    kolvo_chet = 0
    kolvo_nechet = 0
    for digit in str(num):
        if int(digit)%2 == 0: kolvo_chet += 1
        else: kolvo_nechet += 1
    return kolvo_chet, kolvo_nechet


def algo(n):
    n_bin = bin(n)[2:]

    for _ in range(3):
        kolvo_chet, kolvo_nechet = kolvo_cifr(int(n_bin, 2))
        if kolvo_chet > kolvo_nechet:
            n_bin += '1'
        elif kolvo_chet < kolvo_nechet:
            n_bin += '0'
        else:
            n_bin += str(int(n_bin, 2)%2)

    return int(n_bin, 2)


for n in range(10**6):
    if algo(n) > 123455:
        start = n
        break

# for n in range(int(1.25*10**8), 0, -1):
#     if algo(n) < 987_654_321:
#         stop = n
#         break

stop = 123456789

print(stop - start + 1)

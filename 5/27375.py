def tri(n):
    cifri = []

    while n > 0:
        cifri.append(str(n%3))
        n //= 3

    return ''.join(cifri[::-1])



for n in range(1, 1000):
    tri_n = tri(n)

    tri_n += str(n%3)

    r = int(tri_n, 3)

    if r >= 100:
        print(r)
        break

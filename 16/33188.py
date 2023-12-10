# a mod b   ======== a%b
# n - натуральное 0 либо 0 либо >0

def f(n):
    if n == 0: return 0
    elif n%3 == 0: return n + f(n - 3)

    return n + f(n - (n%3))


print(f(22))


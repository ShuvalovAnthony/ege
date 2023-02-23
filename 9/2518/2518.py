import math


f = open('9/2518/2518.txt')

nums = [list(map(int, i.split())) for i in f]

def square(a, b, h): #a - длина, b - ширина, h- высота В ММ!!
    square_in_mm = 2*(a*b + a*h + b*h)
    square_in_dm = square_in_mm/(100**2)
    return square_in_dm


less_than_10_dm = 0
more_than_10_dm = 0


for i in nums:
    if square(*i) < 10:
        less_than_10_dm += 1
    else:
        more_than_10_dm += 1



print(math.ceil(less_than_10_dm/191))
print(math.ceil(more_than_10_dm/103))



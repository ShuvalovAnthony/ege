from turtle import *
from itertools import product


speed(0)

k = 5

def rect(a, b, clr):
    fillcolor(clr)
    begin_fill()
    for _ in range(2):
        fd(a*k)
        rt(90)
        fd(b*k)
        rt(90)
    end_fill()

rect(20, 20, "red")

up()
goto(10*k, 10*k)
down()

rect(20, 20, "blue")

canvas = getcanvas()

counter = 0
for x, y in product(range(-200, 200), repeat=2):
    print(canvas.find_all())
    if canvas.find_overlapping(x*k, y*k, x*k, y*k) != ():
        counter += 1


print(counter)

input()
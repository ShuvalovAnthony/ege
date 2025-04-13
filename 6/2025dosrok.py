from turtle import *

width(10)
rt(90)
tracer(0)
k = 100
screensize(5000, 5000)

rt(30)
for _ in range(3):
    rt(150)
    fd(6*k)
    rt(30)
    fd(12*k)

color('red')
up()
for x in range(-30, 30):
    for y in range(-30, 30):
        goto(x*k, y*k)
        dot(10)

update()


# canvas = getcanvas()
# canvas.postscript(file="/Users/anton/Desktop/drawing.eps")


done()
from turtle import *

tracer(0) # без отрисовки
screensize(5000, 2000)

k = 30 # scale

lt(90) # вверх


# начало фигуры из задания
rt(180)

fd(2*k)
rt(90)
fd(40*k)
rt(90)
fd(2*k)


for i in range(4):
    seth(90)
    circle(-5*k,180)


# сетка из точек
up()
for x in range(-50, 50):
    for y in range(-20, 20):
        goto(x*k, y*k)
        dot(3, "red")


input()
from turtle import *


screensize(5000, 2000)
tracer(0)

k = 50

lt(90)



rt(60)
for i in range(2):
    fd(10*k)
    rt(120)
    fd(5*k)
    rt(240)

rt(120)
fd(3*k)
rt(90)
fd(20*(3**0.5)*k)
rt(90)
fd(8*k)
rt(120)
for i in range(2):
    fd(10*k)
    lt(120)
    fd(5*k)
    lt(240)


up()
for x in range(-20, 20):
    for y in range(-20, 20):
        goto(x*k, y*k)
        dot(3, "red")


input()
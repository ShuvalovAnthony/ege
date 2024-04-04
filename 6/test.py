from turtle import *
# tracer(0)
k = 20
left(90)

begin_fill()
pendown()
for i in range(2):
    forward(10 * k)
    right(90)
    forward(18 * k)
    right(90)
end_fill()
begin_fill()
up()
forward(5 * k)
right(90)
forward(7 * k)
left(90)
down()
for i in range(2):
    forward(10 * k)
    right(90)
    forward(7 * k)
    right(90)
up()
end_fill()

cnt = 0
canvas = getcanvas()
for x in range(-20,20):
    for y in range(-20, 20):
        if canvas.find_overlapping(x*k, y*k, x*k, y*k) != ():
            cnt += 1

print(cnt)
input()

import turtle

t = turtle.Pen()

'''
.forward() / .fd()   - pixels
.backward() / .bk()  - pixels
.right() / .rt()     - degree
.left() / .lt()      - degree
.up() / .down()      - on/off painting
.color()             - 'red' / 'blue' / 'purple'

'''

for i in range(5, 1000):
    t.fd(i)
    t.rt(90)



input()
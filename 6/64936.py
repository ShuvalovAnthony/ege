import turtle

t = turtle.Pen()

"""
.fd() / .forward() - вперед на X пикселей
.bk() / .backward() -  назад на X пикселей
.lt() / .left() - налево на X ГРАДУСОВ!
.rt() / .right() - направо на X ГРАДУСОВ!
.up() / .down() - поднять/опустить перо
.color("red")
.speed() - 1..9 and 0 - maxspeed
"""

# Повтори 4 [Повтори 4 [Вперёд 8 Направо 90] Вперёд 13 Направо 90 Вперёд 4]

t.speed(0)
coords = [(0.00, 0.00)]

def vpered(x: int):
    for i in range(x):
        t.fd(1)
        coords.append(t.pos())

for i in range(4):
    for j in range(4):
        vpered(8)
        t.rt(90)

    vpered(13)
    t.rt(90)
    vpered(4)

print(coords)

# coords = СКОПИРОВАТЬ PRINT() # потом закомментить все, что выше))))

result = set()

for coord in coords:
    if coords.count(coord) > 1:
        result.add(coord)

print(result)
print(len(result))

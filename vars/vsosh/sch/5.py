n = int(input())

showed_digits = []

for i in range(n):
    showed_digits.append(int(input()))

digits = {
    0: [0, 1, 3, 5, 7, 8],
    1: [1, 5, 6],
    2: [8, 5, 2, 0],
    3: [8, 6, 4, 2],
    4: [7, 4, 5, 1],
    5: [8, 7, 4, 1, 0],
    6: [6, 4, 3, 1, 0],
    7: [8, 6, 3],
    8: [8, 7, 5, 4, 3, 1, 0],
    9: [8, 7, 5, 4, 2]
}

works_pins = []

for digit in showed_digits:
    works_pins += digits[digit]

works_pins = set(works_pins)

can_show = []

for key in digits:
    digit_pins = digits[key]
    if set(digit_pins) <= works_pins:
        can_show.append(key)

for i in can_show:
    print(i)
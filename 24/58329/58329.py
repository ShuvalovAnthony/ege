f = open("24/58329/24_58329.txt").read()


digits = [int(i) for i in f]



temp_dlina = 0
max_dlina = 0



for i in range(len(digits) - 2):
    if digits[i] + digits[i + 1] > digits[i + 2]:
        temp_dlina += 1
    else:
        max_dlina = max(max_dlina, temp_dlina + 2)
        temp_dlina = 0


print(max_dlina)
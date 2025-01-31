# f = open("24/58327/24_58327.txt").read()


# max_count = 0
# temp_count = 0

# for i in range(len(f) - 1):
#     current_digit = int(f[i])
#     next_digit = int(f[i + 1])

#     if next_digit <= current_digit:
#         temp_count += 1
#     else:
#         temp_count += 1
#         max_count = max(max_count, temp_count)
#         temp_count = 0


# temp_count += current_digit
# max_count = max(max_count, temp_count)

# print(max_count)



f = open("24/58327/24_58327.txt").read()


max_count = 0
temp_digits = []

for digit in f:
    digit = int(digit)
    if not temp_digits:
        temp_digits.append(digit)
    else:
        if digit > temp_digits[-1]:
            temp_digits.append(digit)
            max_count = max(max_count, len(temp_digits))
            temp_digits = []
        else:
            temp_digits.append(digit)


max_count = max(max_count, len(temp_digits))
temp_digits = []


print(max_count)
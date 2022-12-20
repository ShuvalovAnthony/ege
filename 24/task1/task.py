s = open('24/task1.py/24.txt').read()

start_f_index = 0
last_f_index = 0


max_len = 0
temp_max_len = 0

second_f = False
a_after_last_f = 0


for i in range(len(s)):
    if s[i] == 'F' and not second_f:
        start_f_index = i
        second_f = True
    elif s[i] == 'F':
        temp_max_len = i - start_f_index
        last_f_index = i

    if s[i] == 'A':
        a_after_last_f += 1

    if (a_after_last_f > 2) and last_f_index:
        max_len = max(max_len, temp_max_len)
        start_f_index = last_f_index
    temp_max_len += 1

print(max_len)
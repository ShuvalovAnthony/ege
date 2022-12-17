# 0....7 - цифры

nums = []

for a1 in '1234567': 
    for a2 in '01234567':
        for a3 in '01234567':
            for a4 in '01234567':
                for a5 in '01234567':
                    res = a1 + a2 + a3 + a4 + a5
                    if res.count('6') == 1:
                        nums.append(res)


counter = 0

for num in nums:
    if (num[0] == '6') and (num[1] not in '1357'):
        counter += 1
    elif (num[-1] == '6') and (num[-2] not in '1357'):
        counter += 1
    else:
        ind_six = num.index('6')
        if (num[ind_six - 1] not in '1357') and \
            (num[ind_six + 1] not in '1357'):
            counter += 1

print(counter)

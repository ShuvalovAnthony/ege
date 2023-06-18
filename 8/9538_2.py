counter = 0

for x1 in '123456789ABCDE':
    for x2 in '0123456789ABCDE':
        for x3 in '0123456789ABCDE':
            for x4 in '0123456789ABCDE':
                for x5 in '0123456789ABCDE':
                    res = x1 + x2 + x3 + x4 + x5
                    if ((res[0] in '2468ACE') and (res[2] in '02468ACE') and (res[4] in '02468ACE') and\
                        (res[1] in '0369C') and (res[3] in '0369C')) or\
                        ((res[0] in '0369C') and (res[2] in '0369C') and (res[4] in '0369C') and\
                        (res[1] in '02468ACE') and (res[3] in '02468ACE')):
                            counter += 1


print(counter)


# 0 1 2 3 4 5 6 7 8 9 A B C D E

# 0     3     6     8     C
# 0   2   4   6   8   A   C   E
f = open("24/19149/24_19149.txt").read()



max_len = 0

par_count = 0
curr = ""

def find_max_len(curr):
    try:
        exp = eval(curr)
        if exp%2 == 0:
            return len(curr)
    except:
        return 0

for i in range(len(f)):
    if f[i] == "(":
        par_count += 1
    elif f[i] == ")":
        par_count -= 1
        max_len = max(max_len, find_max_len(curr))
        curr = ""

    if par_count > 0:
        curr += f[i]


print(max_len)
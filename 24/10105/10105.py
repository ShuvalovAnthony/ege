f = open("24/10105/24_10105.txt").read()


t_ind = []

for i in range(len(f)): 
    if f[i] == "T": t_ind.append(i)

max_dlina = 0

for i in range(len(t_ind) - 101):
    # i i+1 i+2 i+3 i+4
    
    # stroka = f[t_ind[i] + 1:t_ind[i+101]]
    len_stroka = t_ind[i+101] - t_ind[i] - 1
    max_dlina = max(max_dlina, len_stroka)


print(max_dlina)
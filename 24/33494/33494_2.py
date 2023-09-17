from collections import Counter

f = open('24/33494/24.txt').read()


res = ''

for i in range(len(f) - 1):
    if f[i] == 'E': res += f[i + 1]


answ_dict = {v:k for k, v in dict(Counter(res)).items()}

print(answ_dict[max(answ_dict)])
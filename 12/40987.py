min_kolvo_edinic = 10**6

for kolvo_edinic in range(200, 1000):
    s = '1'*kolvo_edinic

    while '1111' in s:
        s = s.replace('1111', '22', 1)
        s = s.replace('222', '1', 1)
    
    if s.count('1') < min_kolvo_edinic:
        min_kolvo_edinic = s.count('1')
        print(kolvo_edinic, min_kolvo_edinic)

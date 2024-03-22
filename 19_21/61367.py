def f21(s, step=1): # 1p 2v 3p 4v 5p
    if (s >= 108) and (step in (3, 5)):
        return True
    elif (s >= 108 and step < 5) or (s >= 108 or step == 5):
        return False
    
    if step%2:
        if s % 2 == 0:
            return f21(s + 1, step + 1) and f21(int(s * 1.5), step + 1)  
        else:
            return f21(s + 1, step + 1) and f21(s * 2, step + 1)  
    else:
        if s % 2 == 0:
            return f21(s + 1, step + 1) or f21(int(s * 1.5), step + 1)   
        else:
            return f21(s + 1, step + 1) or f21(s * 2, step + 1)   



print('---21---')
for s in range(1, 108):
    if f21(s):
        print(s)
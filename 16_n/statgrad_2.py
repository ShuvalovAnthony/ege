# https://drive.google.com/drive/folders/10H4yHC55R_MssM23EK3zczJcBLavrC_J



def f(n):
    if n == 0:
        return 0
    return f(n//10) + (n%10)



for i in range(100):
    print(i, f(i) > f(i + 1))

a = 237567892
b = 1134567009

print((b - a)//10)
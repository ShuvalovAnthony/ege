
k = 0

for letter in ('АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЬЫЪЭЮЯ' + '_'*31):
    bin_n = '0'*(6 - len(bin(k)[2::])) + bin(k)[2::]
    print(bin_n, letter)
    k += 1
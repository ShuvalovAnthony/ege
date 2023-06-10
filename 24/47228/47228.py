f = open('24/47228/47228.txt').read()




f = f.replace('O', 'A')\
    .replace('C', 'D')\
    .replace('F', 'D')\
    .replace('DA', '-')\
    .replace('D', ' ')\
    .replace('A', ' ')


# sposob 1 - odnostrochnik
print(
    max(
        [
            len(stroka) for stroka in f.split()
        ]
    )
)


# sposob 2

# result_list = f.split()

# dlini = [len(i) for i in result_list]
# # dlini = list(map(len, dlini))

# max_dlina = max(dlini)

# print(max_dlina)
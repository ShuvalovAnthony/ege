f = open("24/1111/24.txt").read()



glasnie = [ord(i) for i in 'AEIOUY']

chr_codes = [ord(i) for i in f]


sub_words = []

temp_word = []


for i in range(len(chr_codes) - 1):
    if chr_codes[i] < chr_codes[i + 1]:
        temp_word.append(chr_codes[i])
    else:
        temp_word.append(chr_codes[i])
        sub_words.append(temp_word)
        temp_word = []


def count_glas(char_list):
    glas_count = 0
    for glas in glasnie:
        glas_count += char_list.count(glas)
    return glas_count <= 1


def find_max_len(char_list):
    max_len = 0
    for i in range(len(char_list)):
        for j in range(i + 1, len(char_list) + 1):
            sub_list = char_list[i:j]
            if count_glas(sub_list):
                max_len = max(max_len, len(sub_list))
    return max_len



max_len = 0

for sub in sub_words:
    max_len = max(
        max_len,
        find_max_len(sub)
    )


print(max_len)
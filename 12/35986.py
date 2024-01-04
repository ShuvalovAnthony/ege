def algo(stroka: str):
    while '00' not in stroka:
        stroka = stroka.replace('01', '210', 1)
        stroka = stroka.replace('02', '320', 1)
        stroka = stroka.replace('03', '3012', 1)
    return stroka


def check(stroka: str):
    return (stroka.count('1') == 23 and
            stroka.count('2') == 48 and
            stroka.count('3') == 41)


for kolvo_edinic in range(1, 50):
    for kolvo_dvoek in range(1, 50):
        for kolvo_troek in range(1, 50):
            stroka = '0' + '1'*kolvo_edinic +\
                  '2'*kolvo_dvoek + '3'*kolvo_troek + '0'
            if check(
                algo(stroka)
            ):
                print(len(stroka))
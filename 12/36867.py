for edinici in range(1, 100):
    for dvoiki in range(1, 100):
        for troiki in range(1, 100):
            ishod_str = '0' + '1'*edinici + '2'*dvoiki + '3'*troiki + '0'

            while ('00' not in ishod_str):
                ishod_str = ishod_str.replace('01', '210', 1)
                ishod_str = ishod_str.replace('02', '320', 1)
                ishod_str = ishod_str.replace('03', '3012', 1)
            
            if (ishod_str.count('1') == 26) and (ishod_str.count('2') == 54) and (ishod_str.count('3') == 48):
                print(edinici + dvoiki + troiki + 2)
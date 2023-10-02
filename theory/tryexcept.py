nums = [1, 2, 3, 4, 5, 0, -5, -6]


results = []

for num in nums:
    try:
        results.append(55/num)
    except ValueError:
        print('Введи цифры!')
    except ZeroDivisionError:
        print('Скидка не может быть 0')


print(results)
counter = 0

for d1 in (1, 3, 5, 7, 9):
    for d2 in (1, 3, 5, 7, 9):
        for d3 in (1, 3, 5, 7, 9):
            for d4 in (1, 3, 5, 7, 9):
                sum_1_2 = d1 + d2
                sum_3_4 = d3 + d4
                sort_nums = (sorted([sum_1_2, sum_3_4]))
                if str(sort_nums[0]) + str(sort_nums[1]) == "414":
                    counter += 1

print(counter)
f = open("27__/47231/27_A.txt")

labs = [tuple(map(int, i.split())) for i in f]



def cont_num(num_prob, prob_in_one_cont=36):
    return num_prob//prob_in_one_cont + 1*bool(num_prob%prob_in_one_cont)


def del_price(start, stop, num_prob):
    rasst = abs(start - stop)
    c_num = cont_num(num_prob)
    return rasst*c_num



min_price = 10**6


for start_lab in labs:
    temp_min_price = 0
    lab_coord = start_lab[0]
    for lab in labs:
        temp_min_price += del_price(start_lab[0], lab[0], lab[1])
        if temp_min_price > min_price:
            break

    min_price = min(temp_min_price, min_price)


print(min_price)

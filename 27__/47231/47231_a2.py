f = open("ege/27__/47231/27_A.txt")

labs = [tuple(map(int, i.split())) for i in f]



def cont_num(num_prob, prob_in_one_cont=36):
    return num_prob//prob_in_one_cont + 1*bool(num_prob%prob_in_one_cont)


def del_price(start, stop, num_prob):
    rasst = abs(start - stop)
    c_num = cont_num(num_prob)
    return rasst*c_num



for lab in labs:
    print(del_price(0, lab[0], lab[1]))

for n in range(10**8, 10**9):
    bin_n = bin(n)[2:]
    ones = bin_n.count("1")
    zeros = bin_n.count("0")

    res = bin(ones)[2:] + bin(zeros)[2:]


    if res == "10110111":
        print(n)
        break

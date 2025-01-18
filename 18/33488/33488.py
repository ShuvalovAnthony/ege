f = open("18/33488/data.txt")


data = [float(i) for i in f]



max_sum = -10**6



temp_list = []

def get_max_sum(slice: list):
    max_sum = -10**6
    for i in range(len(slice) - 1):
        for j in range(i + 1, len(slice)):
            max_sum = max(max_sum, sum(slice[i:j + 1]))
    return max_sum


for i in range(len(data) - 1):
    if abs(data[i + 1] - data[i]) <= 8:
        temp_list.append(data[i])
    else:
        temp_list.append(data[i])
        
        max_sum = max(max_sum, get_max_sum(temp_list))

        temp_list = []


print(int(max_sum))
# nums = [0, 5, 10, 15, 20, 25]

names = ["alex", "vitya", "boba"]
lastnames = ["klyushkin", "igor", "bobus"]




def full_name(data: list):
    name = data[0]
    lastname = data[1]
    return name + ' ' + lastname


params = [
    [names[i], lastnames[i]] for i in range(3)
]


full_names_list = list(
    map(
    full_name,
    params
    )
)

print(full_names_list)
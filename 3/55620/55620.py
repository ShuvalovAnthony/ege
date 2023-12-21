f = open("3/55620/data.txt")



districts = {
    'Заречный': 0,
    'Центральный': 0,
    'Октябрьский': 0,
    'Первомайский': 0
}


for i in f:
    row = i.split()
    district = row[-1]
    money = float(row[0])

    districts[district] += money


max_value = 0

for i in districts:
    max_value = max(max_value, districts[i])

print(max_value)

print(districts)



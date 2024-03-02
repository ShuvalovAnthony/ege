res = set()
for x in range(10, 67):
    for y in range(67):
        if y < x:
            first = 7*67**4 + 3*67**3 + x*67**2 + 67 + y
            second = 4*x**3 + 9*x**2 + y*x + 6
            res.add(first + second)


print(len(res))
        
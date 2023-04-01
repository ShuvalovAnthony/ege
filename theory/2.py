def f(a, b, c):
    return {"a": a, "b": b, "c": c,}

nums = "АБВ БВГД ВД Д"
ways = {i[0]:i[1:] for i in nums}
print(ways)

# data = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9],
# ]


# for i in data:
#     print(f(*i))
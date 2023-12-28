# nums = set()

# def f(start, stop, limit=5):
#     nums.add(start)

#     if limit == 0: return 0

#     if start == stop: return 1
#     elif start > stop: return 0

#     return (
#         f(start + 1, stop, limit - 1) +
#         f(start*2, stop, limit - 1)
#     )

# f(1, 1000)

# print(sorted(nums))


res = [1]

for i in range(5):
    for num in res.copy():
        res.append(num + 1)
        res.append(num * 2)


print(sorted(set(res)))
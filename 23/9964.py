# from functools import lru_cache


# @lru_cache
# def f(start, stop):
#     if start == stop: return True
#     elif start > stop: return False

#     return (
#         f(start + 1, stop)
#         + f(start*3, stop)
#         + f(start + 5, stop)
#     )


# count = 0
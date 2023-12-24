# def f19(h1, h2, step=1): # 1p 2v 3p 4v 5p 6v
#     if (h1 + h2 >= 77) and (step == 3): return True
#     elif (
#         # если набрали больше чем надо, раньше чем надо
#         ((h1 + h2 >= 77) and (step < 3)) or
#         # если набрали меньше чем надо, тогда когда надо
#         ((h1 + h2 < 77) and (step == 3))
#     ): return False

#     return (
#         f19(h1 + 1, h2, step + 1) or
#         f19(h1, h2 + 1, step + 1) or
#         f19(h1*2, h2, step + 1) or
#         f19(h1, h2*2, step + 1)
#     )


# for h2 in range(1, 70):
#     if f19(7, h2):
#         print(h2)
#         break


# def f20(h1, h2, step=1):  # 1p 2v 3p 4v 5p
#     if (h1 + h2 >= 77) and (step == 4):
#         return True
#     elif (
#         ((h1 + h2 >= 77) and (step < 4)) or
#         ((h1 + h2 < 77) and (step == 4))
#     ):
#         return False

#     if step % 2 == 0:
#         return (
#             f20(h1 + 1, h2, step + 1) and
#             f20(h1, h2 + 1, step + 1) and
#             f20(h1*2, h2, step + 1) and
#             f20(h1, h2*2, step + 1)
#         )

#     return (
#         f20(h1 + 1, h2, step + 1) or
#         f20(h1, h2 + 1, step + 1) or
#         f20(h1*2, h2, step + 1) or
#         f20(h1, h2*2, step + 1)
#     )


# for h2 in range(1, 70):
#     if f20(7, h2):
#         print(h2)



def f21(h1, h2, step=1):  # 1p 2v 3p 4v 5p
    if (h1 + h2 >= 77) and (step in (3, 5)):
        return True
    elif (
        ((h1 + h2 >= 77) and (step < 5)) or
        ((h1 + h2 < 77) and (step == 5))
    ):
        return False

    if step % 2 == 1:
        return all(
            [f21(h1 + 1, h2, step + 1),
            f21(h1, h2 + 1, step + 1),
            f21(h1*2, h2, step + 1),
            f21(h1, h2*2, step + 1)]
        )

    return any(
        [f21(h1 + 1, h2, step + 1),
        f21(h1, h2 + 1, step + 1),
        f21(h1*2, h2, step + 1),
        f21(h1, h2*2, step + 1)]
    )


for h2 in range(1, 70):
    if f21(7, h2):
        print(h2)
        break
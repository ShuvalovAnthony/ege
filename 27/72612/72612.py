from math import dist


# f = open("ege/27/72612/27a.txt")
f = open("ege/27/72612/27b.txt")

dots = [
    [float(i) for i in row.split()] for row in f
]

# # файл А
# # условия из экселя
# claster1 = [
#     dot for dot in dots if (
#         (-1 <= dot[0] <= 2) and (6 <= dot[1] <= 9)
#     )
# ]

# claster2 = [
#     dot for dot in dots if (
#         (0 <= dot[0] <= 3) and (3 <= dot[1] <= 6)
#     )
# ]

# claster3 = [
#     dot for dot in dots if (
#         (-2 <= dot[0] <= 1) and (-1 <= dot[1] <= 2)
#     )
# ]

# # убираем минимальный
# clasters = sorted([claster1, claster2, claster3])[1:]


# Файл В
# условия из экселя
claster1 = [
    dot for dot in dots if (
        (-2.5 <= dot[0] <= .5) and (-1.5 <= dot[1] <= 1.5)
    )
]

claster2 = [
    dot for dot in dots if (
        (.5 <= dot[0] <= 2.5) and (3 <= dot[1] <= 5.5)
    )
]

claster3 = [
    dot for dot in dots if (
        (4 <= dot[0] <= 7) and (5 <= dot[1] <= 8)
    )
]

claster4 = [
    dot for dot in dots if (
        (3.5 <= dot[0] <= 6.5) and (1.5 <= dot[1] <= 4.5)
    )
]

claster5 = [
    dot for dot in dots if (
        (3 <= dot[0] <= 6.5) and (-2.5 <= dot[1] <= 1.5)
    )
]

# убираем минимальный
clasters = sorted(
    [claster1, claster2, claster3, claster4, claster5],
    key=lambda x: len(x)
    )[:-1]

# print([len(i) for i in clasters])
# поиск центроиды
def find_claster_center(claster: list):
    min_summa_dist = 10**6
    center = None

    for i in range(len(claster)):
        temp_min_summa_dist = 0
        for j in range(len(claster)):
            temp_min_summa_dist += dist(claster[i], claster[j])
            
        if temp_min_summa_dist <= min_summa_dist:
            min_summa_dist = temp_min_summa_dist
            center = claster[i]

    return center

centroids = [find_claster_center(claster) for claster in clasters]

middle_point = (
    int(10000*sum([centroid[0] for centroid in centroids])/len(centroids)),
    int(10000*sum([centroid[1] for centroid in centroids])/len(centroids)),
)

print(middle_point)


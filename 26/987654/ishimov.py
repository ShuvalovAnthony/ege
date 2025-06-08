f = open("ege/26/987654/26.txt")


n, m, k = [int(i) for i in f.readline().split()]

dots = [
    [int(i) for i in row.split()] for row in f
]

board = [[0 for i in range(k + 1)] for j in range(m + 1)]


for row, col in dots:
    board[row][col] = 1

# for row in board:
#     print(*row)

def isLeftTopCorner(row, col):
    if board[row][col] != 1: return False
    if (row == 1) and (col == 1): return True
    if (row == 1) and (board[row][col - 1] == 0): return True
    if (board[row - 1][col] == 0) and (col == 1): return True
    if (board[row - 1][col] == 0) and (board[row][col - 1] == 0): return True
    return False


def findArea(row, col):
    vert_len = 0
    hor_len = 0
    for row_ in range(row, m):
        if board[row_][col] == 1:
            vert_len += 1

    for col_ in range(col, k):
        if board[row][col_] == 1:
            hor_len += 1

    return (vert_len, hor_len)

ships = []

for row in range(m):
    for col in range(k):
        if isLeftTopCorner(row, col):
            # print("CORNER", row, col)
            x, y = findArea(row, col)
            if x*y >= 6000:
                print([row, col + y - 1]) # 1ое подойдет
                # exit()
                ships.append([row, col + y - 1])

print(ships)


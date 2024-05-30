H = int(input())
board = [list(input()) for _ in range(H)]

directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]

while True:
    delete_happened = False
    delete_set = set()
    for y in range(H):
        for x in range(5):
            deletable = True
            for dy, dx in directions:
                if 0 <= y + dy < H and 0 <= x + dx < 5:
                    if board[y + dy][x+dx] != board[y][x] or board[y][x] == ".":
                        deletable = False
                        break
            if deletable:
                delete_set.add((y,x))
                for dy, dx in directions:
                    if 0 <= y + dy < H and 0 <= x + dx < 5:
                        delete_set.add((y + dy, x + dx))
                delete_happened = True

    if delete_happened == False:
        break
    else:
        for y,x in delete_set:
            if 0 <= y < H and 0 <= x < 5:
                board[y][x] = "."

    for i in range(H-1, -1, -1):
        for j in range(5):
            drop_size = 0
            for k in range(1, H+1):
                if 0 <= i+ k < H and board[i+k][j] == ".":
                    drop_size += 1
                else:
                    break
            if drop_size != 0:
                board[i+drop_size][j] = board[i][j]
                board[i][j] = "."

for row in board:
    print("".join(row))
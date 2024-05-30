def check_adjacent(board, y, x, directions):
    for dy, dx in directions:
        if not (0 <= y + dy < len(board) and 0 <= x + dx < 5):
            return False
        if board[y + dy][x + dx] != board[y][x] or board[y][x] == ".":
            return False
    return True

def delete_elements(board, delete_set):
    for y, x in delete_set:
        if 0 <= y < len(board) and 0 <= x < 5:
            board[y][x] = "."

def drop_elements(board):
    for j in range(5):
        for i in range(len(board) - 1, -1, -1):
            drop_size = 0
            for k in range(1, len(board) - i + 1):
                if 0 <= i + k < len(board) and board[i + k][j] == ".":
                    drop_size += 1
                else:
                    break        
            if drop_size != 0:
                board[i + drop_size][j], board[i][j] = board[i][j], "."

def cross_puzzle():
    H = int(input())
    board = [list(input()) for _ in range(H)]

    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]

    while True:
        delete_set = set()
        for y in range(len(board)):
            for x in range(5):
                if check_adjacent(board, y, x, directions):
                    delete_set.add((y, x))
                    for dy, dx in directions:
                        delete_set.add((y + dy, x + dx))

        if not delete_set:
            break

        delete_elements(board, delete_set)
        drop_elements(board)

    for row in board:
        print("".join(row))

cross_puzzle()
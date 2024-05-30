from collections import deque

H, W = input().split()
board = [list(input()) for _ in range(int(H))]

moves = [(-1, 0), (0, 1), (1, 0), (0, -1)]

for i in range(int(H)):
    if "*" in board[i]:
        y = i
        x = board[i].index("*")

queue = deque()
queue.append((y, x))

while queue:
    queue.popleft()
    for move in moves:
        dy , dx = move
        if 0 <= y + dy < int(H) and 0 <= x + dx < int(W) and board[y+dy][x+dx] != "#":
            board[y+dy][x+dx] = "*"
            queue.append((y+dy, x+dx))
        

for row in board:
    print("".join(row))
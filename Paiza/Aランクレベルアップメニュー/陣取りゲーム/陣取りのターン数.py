from collections import deque

H, W, N = map(int, input().split())
board = [list(input()) for _ in range(H)]
l = [int(input()) for _ in range(N)]

moves = [(-1, 0), (0, 1), (1, 0), (0, -1)]

# 開始地点を探す
for i in range(H):
    if "*" in board[i]:
        y, x = i, board[i].index("*")
        break

queue = deque([(y, x, 0)])  # (y, x, 距離)
if 0 in l:
    board[y][x] = "?"

while queue:
    y, x, dist = queue.popleft()
    
    for dy, dx in moves:
        ny, nx = y + dy, x + dx
        if 0 <= ny < H and 0 <= nx < W and board[ny][nx] == '.':
            if dist+1 in l:
                board[ny][nx] = "?"
            else:
                board[ny][nx] = "*"
            queue.append((ny, nx, dist + 1))

for row in board:
    print("".join(row))
# 自分の解答
def toggle(cell):
    return "#" if cell == "." else "."

H, W = map(int, input().split())
board = []
for i in range(H):
    S = input()
    board.append(list(S))
y,x = map(int, input().split())

# 横方向をすべて反転
for i in range(W):
    board[y][i] = toggle(board[y][i])
# 縦方向を(既に反転したセルを除き)すべて反転 
for i in range(H):
    if i != y:  # 既に反転されたセルはスキップ
        board[i][x] = toggle(board[i][x])

# 斜め方向をすべて反転
for a in range(H):
    for dy, dx in [(a,a), (-a, a), (-a, -a), (a,-a)]: # (0, 0)は既に反転しているので除外
        ny, nx = y + dy, x + dx
        if 0 <= ny < H and 0 <=nx < W:
            board[ny][nx] = toggle(board[ny][nx])

for i in range(H):
    print("".join(board[i]))
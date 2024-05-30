from collections import deque

# 入力の取得
H, W = map(int, input().split())
board = [list(input()) for _ in range(H)]

# 移動方向のリスト (上、右、下、左)
moves = [(-1, 0), (0, 1), (1, 0), (0, -1)]

# スタート位置（'*'）を探す
for i in range(H):
    if "*" in board[i]:
        y = i
        x = board[i].index("*")
        break

# キューを初期化し、スタート位置を追加
queue = deque([(y, x, 0)])  # (y, x, 距離)

# スタート位置を探索済みとしてマーク
board[y][x] = '0'

while queue:
    y, x, dist = queue.popleft()
    
    # 各移動方向について探索
    for dy, dx in moves:
        ny, nx = y + dy, x + dx
        
        # 範囲内かどうかの確認と、未探索（'.'）かどうかの確認
        if 0 <= ny < H and 0 <= nx < W and board[ny][nx] == '.':
            board[ny][nx] = str(dist + 1)  # 距離をマーク
            queue.append((ny, nx, dist + 1))

# 結果の表示
for row in board:
    print("".join(row))

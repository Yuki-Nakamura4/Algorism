from collections import deque

# 入力を取得
H, W = map(int, input().split())
N = input().strip()
board = [list(input().strip()) for _ in range(H)]

# 移動の方向
moves = [(-1, 0), (0, 1), (1, 0), (0, -1)]

# 開始地点を探す
ay = ax = by = bx = -1
for i in range(H):
    if "A" in board[i] and ay == -1:
        ay, ax = i, board[i].index("A")
    if "B" in board[i] and by == -1:
        by, bx = i, board[i].index("B")

a_queue = deque([(ay, ax)])
b_queue = deque([(by, bx)])

# 最初のターンを設定
turn = N
count_a = 1
count_b = 1

# ゲームのループ
while a_queue or b_queue:
    if turn == "A":
        if a_queue:
            # 現在のAの陣地から次のマスを占領する
            for _ in range(len(a_queue)):
                ay, ax = a_queue.popleft()
                for dy, dx in moves:
                    ny, nx = ay + dy, ax + dx
                    if 0 <= ny < H and 0 <= nx < W and board[ny][nx] == '.':
                        board[ny][nx] = "A"
                        count_a += 1
                        a_queue.append((ny, nx))
        turn = "B"
    elif turn == "B":
        if b_queue:
            # 現在のBの陣地から次のマスを占領する
            for _ in range(len(b_queue)):
                by, bx = b_queue.popleft()
                for dy, dx in moves:
                    ny, nx = by + dy, bx + dx
                    if 0 <= ny < H and 0 <= nx < W and board[ny][nx] == '.':
                        board[ny][nx] = "B"
                        count_b += 1
                        b_queue.append((ny, nx))
        turn = "A"

# 結果を出力
print(count_a, count_b)
winner = "A" if count_a > count_b else "B"
print(winner)

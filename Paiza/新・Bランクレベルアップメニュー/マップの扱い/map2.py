# # 自分の解答
# H, W = map(int, input().split())
# board = []
# for i in range(H):
#     S = input()
#     board.append(list(S))
# y,x= map(int, input().split())

# if y>0:
#     if board[y-1][x] == ".":
#         board[y-1][x] = "#"
#     else:
#           board[y-1][x] = "."
# if x > 0:
#     if board[y][x-1] == ".":
#         board[y][x-1] = "#"
#     else:
#           board[y][x-1] = "."
# if board[y][x] == ".":
#     board[y][x] = "#"
# else:
#     board[y][x] = "." 
# if x < W-1:        
#     if board[y][x+1] == ".":
#         board[y][x+1] = "#"
#     else:
#         board[y][x+1] = "." 
# if y < H-1:        
#     if board[y+1][x] == ".":
#         board[y+1][x] = "#"
#     else:
#         board[y+1][x] = "." 
# for i in range(H):
#     print("".join(board[i]))

# 模範解答：
# “.”と”#”を反転させる処理はtoggleという関数にまとめた
# 上下左右の座標は変化量を[(-1, 0), (1, 0), (0, -1), (0, 1), (0, 0)]という配列にまとめ、
# 中心の座標と組み合わせることで表現した

# "."と"#"を反転させる関数
def toggle(cell):
    return "#" if cell == "." else "."

H, W = map(int, input().split())
board = []
for i in range(H):
    S = input()
    board.append(list(S))
y, x = map(int, input().split())

# 現在のセルと隣接するセルを反転させる
for dy, dx in [(-1, 0), (1, 0), (0, -1), (0, 1), (0, 0)]: # dyはdelta_yでyの変化量
    new_y, new_x = y + dy, x + dx
    if 0 <= new_y < H and 0 <= new_x < W: # 範囲外はスキップ
        board[new_y][new_x] = toggle(board[new_y][new_x])

# 結果を出力
for row in board:
    print("".join(row))
# 自分の解答
H, W = map(int, input().split())

board = []

for i in range(H):
    S =input()
    board.append(list(S)) # 配列に変換して保持
    
x, y = map(int, input().split())

if board[x][y] == ".":
    board[x][y] = "#"
else:
     board[x][y] = "."
     
for i in range(H):
    print("".join(board[i])) # 結合して文字列として出力
    
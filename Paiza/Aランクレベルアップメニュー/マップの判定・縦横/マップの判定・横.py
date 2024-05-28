# # 自分の解答
# # 冗長
# # 最終行で整数配列のまま `” “.join()` をしようとしたところエラーが出た
# # 要素を文字列に変換してからでないと連結できない
# H, W = map(int, input().split())

# board=[]
# for i in range(H):
#     S = list(input())
#     board.append(S)

# ans = []

# for i in range(H):
#     for j in range(W):
#         if j -1 < 0:
#             if board[i][j + 1] == "#":
#                 ans.append([i,j])
#         elif j +1 > W -1:
#             if board[i][j - 1] == "#":
#                 ans.append([i,j])
#         else:
#             if board[i][j - 1] == "#" and board[i][j + 1] == "#":
#                 ans.append([i,j])

# for point in ans:
#     print(" ".join(map(str, point))) 

# 模範解答
h, w = map(int, input().split())
s = [list(input()) for _ in range(h)]

for y in range(h):
    for x in range(w):
        if x == 0 or s[y][x - 1] == "#":
            if x == w - 1 or s[y][x + 1] == "#":
                print(y, x)
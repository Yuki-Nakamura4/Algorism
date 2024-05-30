H, W = input().split()
board = [list(input()) for _ in range(int(H))]

moves = [(-1, 0), (0, 1), (1, 0), (0, -1)]

for i in range(int(H)):
    if "*" in board[i]:
        y = i
        x = board[i].index("*")

for move in moves:
    dy , dx = move
    if 0 <= y + dy < int(H) and 0 <= x + dx < int(W):
        board[y+dy][x+dx] = "*"

for row in board:
    print("".join(row))


# # 模範解答
# H, W = map(int, input().split())
# s = [list(input()) for _ in range(H)]
#
# flag_out = False
# for y in range(H):
#     for x in range(W):
#         if s[y][x] == "*":
#             if y > 0:
#                 s[y - 1][x] = "*"
#             if y < H - 1:
#                 s[y + 1][x] = "*"
#             if x > 0:
#                 s[y][x - 1] = "*"
#             if x < W - 1:
#                 s[y][x + 1] = "*"
#             flag_out = True
#             break
#     if flag_out:
#         break

# for y in range(H):
#     print("".join(s[y]))
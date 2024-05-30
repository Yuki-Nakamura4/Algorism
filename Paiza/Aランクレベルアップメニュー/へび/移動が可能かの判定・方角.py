# H, W, sy, sx, m = input().split()
# H, W, sy, sx = int(H), int(W), int(sy), int(sx)
# board = [input() for _ in range(H)]

# if m == "N":
#     if board[sy-1][sx] == "." and sy-1 >= 0:
#         print("Yes")
#     else:
#         print("No")
# elif m == "E":
#     if board[sy][sx+1] == "." and sx+1 < W:
#         print("Yes")
#     else:
#         print("No")
# elif m == "S":
#     if board[sy+1][sx] == "." and sy+1 < H:
#         print("Yes")
#     else:
#         print("No")
# elif m == "W":
#     if board[sy][sx-1] == "." and sx-1 >= 0:
#         print("Yes")
#     else:
#         print("No")

# 模範解答
# まとめられる処理はまとてある
h, w, sy, sx, m = input().split()
s = [list(input()) for _ in range(int(h))]
sy = int(sy)
sx = int(sx)

if m == "N":
    sy -= 1
elif m == "E":
    sx += 1
elif m == "S":
    sy += 1
elif m == "W":
    sx -= 1

if sx < 0 or sx >= int(w) or sy < 0 or sy >= int(h) or s[sy][sx] == "#":
    print("No")
else:
    print("Yes")
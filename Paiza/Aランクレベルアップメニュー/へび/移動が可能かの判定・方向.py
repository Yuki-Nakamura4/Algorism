# # 自分の解答
# # forwardをインデックスとしても文字列としても使ってるのはよくないかもしれない
# h, w, sy, sx, n = map(int, input().split())
# s = [list(input()) for _ in range(int(h))]
# d = [input() for _ in range(int(n))]

# directions = ["N", "E", "S", "W"]
# forward = "N"

# for move_d in d:
#     if  move_d == "L":
#         forward = (3 + directions.index(forward)) % 4
#     else:
#         forward = (1 + directions.index(forward)) % 4

#     if directions[forward] == "N":
#         sy -= 1
#     elif directions[forward] == "E":
#         sx += 1
#     elif directions[forward] == "S":
#         sy += 1
#     elif directions[forward] == "W":
#         sx -= 1
#     forward = directions[forward]

#     if sx < 0 or sx >= int(w) or sy < 0 or sy >= int(h) or s[sy][sx] == "#":
#         print("Stop")
#         break
#     else:
#         print(sy, sx)


# 模範解答
# こうすればスッキリ
h, w, sy, sx, n = input().split()
s = [list(input()) for _ in range(int(h))]
sy = int(sy)
sx = int(sx)
directions = ["N", "E", "S", "W"]
now = 0

for _ in range(int(n)):
    d = input()
    if d == "L":
        now = (3 + now) % 4
    else:
        now = (1 + now) % 4

    if directions[now] == "N":
        sy -= 1
    elif directions[now] == "E":
        sx += 1
    elif directions[now] == "S":
        sy += 1
    elif directions[now] == "W":
        sx -= 1

    if sx < 0 or sx >= int(w) or sy < 0 or sy >= int(h) or s[sy][sx] == "#":
        print("Stop")
        break
    else:
        print(sy, sx)
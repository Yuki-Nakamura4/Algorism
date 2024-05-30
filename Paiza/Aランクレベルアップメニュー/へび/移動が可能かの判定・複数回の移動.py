# 自分の解答
h, w, sy, sx, n = map(int, input().split())
s = [list(input()) for _ in range(int(h))]
d = [input() for _ in range(int(n))]

directions = ["N", "E", "S", "W"]

for move_d in d:
    if  move_d == "L":
        forward = (3 + directions.index(move_d)) % 4
    else:
        forward = (1 + directions.index(move_d)) % 4

    if directions[forward] == "N":
        sy -= 1
    elif directions[forward] == "E":
        sx += 1
    elif directions[forward] == "S":
        sy += 1
    elif directions[forward] == "W":
        sx -= 1

    if sx < 0 or sx >= int(w) or sy < 0 or sy >= int(h) or s[sy][sx] == "#":
        print("STOP")
        break
    else:
        print(sy, sx)
h, w, sy, sx, n = input().split()
board = [list(input()) for _ in range(int(h))]
sy = int(sy)
sx = int(sx)
directions = ["N", "E", "S", "W"]
now = 0

board[sy][sx] = "*"

for _ in range(int(n)):
    d, l = input().split()
    l = int(l)
    if d == "L":
        now = (3 + now) % 4
    else:
        now = (1 + now) % 4

    stop_flag = False
    for _ in range(l):
        prev_sx, prev_sy = sx, sy
        if directions[now] == "N":
            sy -= 1
        elif directions[now] == "E":
            sx += 1
        elif directions[now] == "S":
            sy += 1
        elif directions[now] == "W":
            sx -= 1
        
        if sx < 0 or sx >= int(w) or sy < 0 or sy >= int(h) or board[sy][sx] == "#":
            stop_flag = True
            break
        else:
            board[sy][sx] = "*"
    
    if stop_flag:
        break
    
for row in board:
    print("".join(row))
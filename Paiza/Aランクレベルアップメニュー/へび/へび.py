h, w, sy, sx, n = input().split()
sy, sx = int(sy), int(sx)
board = [list(input()) for _ in range(int(h))]
move_d = []
time = []
for i in range(int(n)):
    t, d = input().split()
    t = int(t)
    move_d.append(d)
    time.append(t)

directions = ["N", "E", "S", "W"]
forward = 0 # 初期値は北

board[sy][sx] = "*" # 初期位置も+とする

for i in range(100):
    prev_sx, prev_sy = sx, sy   
    
    # もし時間が来たら方向転換
    if i in time:
        index = time.index(i)
        if  move_d[index] == "L":
            forward = (3 + forward) % 4
        else:
            forward = (1 + forward) % 4
        
    if directions[forward] == "N":
        sy -= 1
    elif directions[forward] == "E":
        sx += 1
    elif directions[forward] == "S":
        sy += 1
    elif directions[forward] == "W":
        sx -= 1
        
    if sx < 0 or sx >= int(w) or sy < 0 or sy >= int(h) or board[sy][sx] == "#" or board[sy][sx] == "*":
        break
    else:
        board[sy][sx] = "*"
    
for row in board:
    print("".join(row))
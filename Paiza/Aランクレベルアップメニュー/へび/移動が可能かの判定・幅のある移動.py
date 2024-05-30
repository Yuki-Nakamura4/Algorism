h, w, sy, sx, n = input().split()
s = [list(input()) for _ in range(int(h))]
sy = int(sy)
sx = int(sx)
directions = ["N", "E", "S", "W"]
now = 0

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
        
        if sx < 0 or sx >= int(w) or sy < 0 or sy >= int(h) or s[sy][sx] == "#":
            stop_flag = True
            break
    
    if stop_flag == True:
        print(prev_sy, prev_sx)
        print("Stop")
        break
    else:
        print(sy, sx)

# 模範解答
# 似た感じ
h, w, sy, sx, n = input().split()
s = [list(input()) for _ in range(int(h))]
sy = int(sy)
sx = int(sx)
directions = ["N", "E", "S", "W"]
now = 0

for _ in range(int(n)):
    d_i, l_i = input().split()
    l_i = int(l_i)
    if d_i == "L":
        now = (3 + now) % 4
    else:
        now = (1 + now) % 4

    flag = False
    for i in range(l_i):
        if directions[now] == "N":
            sy -= 1
        elif directions[now] == "E":
            sx += 1
        elif directions[now] == "S":
            sy += 1
        elif directions[now] == "W":
            sx -= 1

        if sx < 0 or sx >= int(w) or sy < 0 or sy >= int(h) or s[sy][sx] == "#":
            flag = True
            if directions[now] == "N":
                sy += 1
            elif directions[now] == "E":
                sx -= 1
            elif directions[now] == "S":
                sy -= 1
            elif directions[now] == "W":
                sx += 1
            break

    print(sy, sx)
    if flag:
        print("Stop")
        break
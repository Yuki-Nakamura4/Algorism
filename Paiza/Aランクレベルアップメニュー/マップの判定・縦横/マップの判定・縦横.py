H, W = map(int, input().split())
S = [list(input()) for _ in range(H)]

for y in range(H):
    for x in range(W):
        if x == 0 or S[y][x - 1] == "#":
            if x == W - 1 or S[y][x + 1] == "#":
                if y == 0 or S[y-1][x] == "#":
                    if y == H - 1 or S[y+1][x] == "#":
                        print(y, x)
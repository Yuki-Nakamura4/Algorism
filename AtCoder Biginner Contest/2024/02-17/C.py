H, W, N = map(int, input().split())
T = input()
S = [input() for _ in range(H)]


def move(i, j):
    for t in range(len(T)):
        if T[t] == "U":
            i -= 1
            if S[i][j] == "#":
                return False
        elif T[t] == "D":
            i += 1
            if S[i][j] == "#":
                return False
        elif T[t] == "L":
            j -= 1
            if S[i][j] == "#":
                return False
        elif T[t] == "R":
            j += 1
            if S[i][j] == "#":
                return False
    return True


count = 0

for i in range(1, H - 1):
    for j in range(1, W - 1):
        if S[i][j] == "#":
            continue
        else:
            if move(i, j):
                count += 1

print(count)

# 模範解答
# H, W, N = map(int, input().split())
# T = input()
# S = [input() for _ in range(H)]

# ans = 0
# for i in range(H):
#     for j in range(W):
#         y, x = i, j
#         ok = S[y][x] =="."
#         for c in T:
#             if not ok:
#                 break
#             if c == "L":
#                 x -= 1
#             elif c == "R":
#                 x += 1
#             elif c == "U":
#                 y -= 1
#             elif c == "D":
#                 y += 1
#             ok &= S[y][x] == "."
#         ans += ok
# print(ans)

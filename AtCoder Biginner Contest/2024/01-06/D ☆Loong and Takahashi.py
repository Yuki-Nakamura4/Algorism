# 模範解答

N = int(input())
a = [[0] * N for _ in range(N)]
y, x, c = 0, -1, 0
for i in range(N // 2):
    for j in range(N - i * 2):
        x += 1
        c += 1
        a[y][x] = c
    for j in range(N - i * 2 - 1):
        y += 1
        c += 1
        a[y][x] = c
    for j in range(N - i * 2 - 1):
        x -= 1
        c += 1
        a[y][x] = c
    for j in range(N - i * 2 - 2):
        y -= 1
        c += 1
        a[y][x] = c
a[y][x + 1] = "T"
for r in a:
    print(*r)

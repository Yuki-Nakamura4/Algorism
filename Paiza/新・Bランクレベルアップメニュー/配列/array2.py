# 模範解答

N = int(input())
A = [[list(map(int, input().split())) for _ in range(N)] for _ in range(N)]

ans = 0

for x in range(N): # すべてのx平面について
    for i in range(N):
        row_sum = 0
        for j in range(N):
            row_sum += A[x][i][j]
        ans = max(row_sum, ans)

for y in range(N): # すべてのy平面について
    for i in range(N):
        row_sum = 0
        col_sum = 0
        for j in range(N):
            row_sum += A[i][y][j]
            col_sum += A[j][y][i]
        ans = max(row_sum, col_sum, ans)

for z in range(N):
    for i in range(N):
        row_sum = 0
        col_sum = 0
        for j in range(N):
            row_sum += A[i][j][z]
            col_sum += A[j][i][z]
        ans = max(row_sum, col_sum, ans)

for x in range(N):
    left_right_down = 0
    left_right_up = 0
    for i in range(N):
        left_right_down += A[x][i][i]
        left_right_up += A[x][N - 1 - i][i]
    ans = max(left_right_down, left_right_up, ans)

for y in range(N):
    left_right_down = 0
    left_right_up = 0
    for i in range(N):
        left_right_down += A[i][y][i]
        left_right_up += A[i][y][N - 1 - i]
    ans = max(left_right_down, left_right_up, ans)

for z in range(N):
    left_right_down = 0
    left_right_up = 0
    for i in range(N):
        left_right_down += A[i][i][z]
        left_right_up += A[i][N - 1 - i][z]
    ans = max(left_right_down, left_right_up, ans)

l_1 = 0
l_2 = 0
l_3 = 0
l_4 = 0

for i in range(N):
    l_1 += A[i][i][i]
    l_2 += A[i][N - 1 - i][N - 1 - i]
    l_3 += A[i][N - 1 - i][i]
    l_4 += A[i][i][N - 1 - i]

ans = max(ans, l_1, l_2, l_3, l_4)

print(ans)
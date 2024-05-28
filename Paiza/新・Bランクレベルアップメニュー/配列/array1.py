# 自分の解答
N = int(input())
table = []

for i in range(N):
    A = list(map(int, input().split()))
    table.append(A)

max_num = 0

for i in range(N):
    amount = 0
    for j in range(N):
        amount += table[i][j]
    max_num = max(max_num, amount)

for i in range(N):
    amount = 0
    for j in range(N):
        amount += table[j][i]
    max_num = max(max_num, amount)

amount = 0
for i in range(N):
    amount += table[i][i]
max_num = max(max_num, amount)

amount = 0
for i in range(N):
    amount += table[i][N - i - 1]
max_num = max(max_num, amount)

print(max_num)


# # 模範解答
# N = int(input())
# A = []

# for _ in range(N):
#     A.append(list(map(int, input().split())))

# ans = 0

# for i in range(N):
#     row_sum = 0
#     col_sum = 0
#     for j in range(N):
#         row_sum += A[i][j]
#         col_sum += A[j][i]
#     ans = max(row_sum, col_sum, ans)

# left_right_down = 0
# left_right_up = 0

# for i in range(N):
#     left_right_down += A[i][i]
#     left_right_up += A[N - 1 - i][i]

# ans = max(left_right_down, left_right_up, ans)

# print(ans)
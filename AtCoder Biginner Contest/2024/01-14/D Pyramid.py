# https://www.youtube.com/watch?v=g2-e1ntHOq4

# 模範解答

N = int(input())
A = [0] + list(map(int, input().split()))

l, r = [0] * (N + 2), [0] * (N + 2)

# l[i] = i番目のブロックを頂点としたとき左下に伸ばせる最大の長さ
for i in range(1, N + 1):
    l[i] = min(A[i], l[i - 1] + 1)

# r[i] = i番目の頂点としたとき右下に伸ばせる最大の長さ
for i in range(N, 0, -1):
    r[i] = min(A[i], r[i + 1] + 1)

# 各頂点におけるlとrの最小値のうち、最大値を求める
print(max(min(l[i], r[i]) for i in range(1, N + 1)))


# N = int(input())

# A = list(map(int, input().split()))

# # 2k-1 = N => k = (N+1)//2が最大値

# ans = 0

# top = (N+1)//2

# flag = True

# for k in range(top, 0, -1):
#     for i in range(0, top):
#         if A[i] < i+1:
#             flag = False
#             break
#         else:
#             continue
#     for j in range(top, N):
#         if A[j] < N-j:
#             flag = False
#             break
#         else:
#             continue

#     if flag:
#         print(top)

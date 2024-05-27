# 自分の解答
N, K = map(int, input().split())
P =[]
for _ in range(N):
    P.append(int(input()))

max_price = 0

for i in range(N):
    price = 0
    for j in range(i, i+K):
        price += P[j%N] # 一周すると0に戻るためNで割った余りにする
    max_price = max(max_price, price)

print(max_price)

# # 模範解答
# N, K = map(int, input().split())
# P = [int(input()) for _ in range(N)]

# ans = 0

# for i in range(N):
#     sum_ = 0
#     for j in range(K):
#         sum_ += P[(i + j) % N]
#     ans = max(ans, sum_)

# print(ans)
# 模範解答
# 制約が1 ≦ N ≦ 15なので素直に全探索する。O(2^N * N)かかる
# bit全探索を使用
n, X = map(int, input().split())
w = [int(input()) for _ in range(n)]
ans = 0

# 2のn乗は1<<nとして計算
for i in range(1 << n): # シフトにより空いた右端には0が格納される
    sum_ = 0
    tmp = i
    for j in range(n):
        if tmp % 2 == 1:
            sum_ += w[j]
        tmp //= 2
    
    if sum_ <= X:
        ans = max(ans, sum_)

print(ans)

# 動的計画法を用いるとより高速
# O(N * X)で済む
# ただしDPテーブルを保持する分空間計算量はO(N*X)かかってしまう
def knapsack_max_sum(weights, X):
    n = len(weights)
    dp = [[0] * (X + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(1, X + 1):
            if weights[i - 1] <= j:
                dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - weights[i - 1]] + weights[i - 1])
            else:
                dp[i][j] = dp[i - 1][j]

    return dp[n][X]

n, X = map(int, input().split())
w = [int(input()) for _ in range(n)]

# 答えの計算と出力
print(knapsack_max_sum(w, X))

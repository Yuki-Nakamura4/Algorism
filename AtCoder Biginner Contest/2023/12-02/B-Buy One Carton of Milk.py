# 動的計画法で解く問題
# 最小金額を求める問題

N, S, M, L = map(int, input().split())

dp = [float("inf")] * (N + 12)
dp[0] = 0

for i in range(1, N + 12):
    if i >= 6:
        dp[i] = min(dp[i], dp[i - 6] + S)
    if i >= 8:
        dp[i] = min(dp[i], dp[i - 8] + M)
    if i >= 12:
        dp[i] = min(dp[i], dp[i - 12] + L)

result = min(dp[N : N + 12])
print(result)

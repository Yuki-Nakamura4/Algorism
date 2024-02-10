# 入力の受け取り
S = input()
# 文字数=N
N = len(S)

# Sの0文字目を?にする
S = "?" + S
# T=?chokudai(?は0文字目)
T = "?chokudai"

# 余りの定義
mod = 10**9 + 7

# (1)表を作る
dp = [[0] * 9 for i in range(N + 1)]

# (2)すぐにわかるところを埋める
# i=0~N
for i in range(N + 1):
    # k=0
    dp[i][0] = 1

# (3)表の小さい方から答えにたどり着くまで埋める
# Sのi文字目までを使う
for i in range(1, N + 1):
    # chokudaiのk文字目までを作る
    for k in range(1, 9):
        # 1≤i≤N,1≤k≤8,Sのi文字目=chokudaiのk文字目の場合
        if S[i] == T[k]:
            # dp[i-1][k]：Sの(i-1)文字目までを使ってchokudaiのk文字目を作る場合(Sのi文字目を使わない)
            # dp[i-1][k-1]：Sの(i-1)文字目までを使ってchokudaiの(k-1)文字目を作る場合(Sのi文字目を使う)
            dp[i][k] = dp[i - 1][k] + dp[i - 1][k - 1]

        # 1≤i≤N,1≤k≤8,Sのi文字目≠chokudaiのk文字目の場合
        else:
            # dp[i-1][k-1]：Sの(i-1)文字目までを使ってchokudaiの(k-1)文字目を作る場合(Sのi文字目を使う)
            dp[i][k] = dp[i - 1][k]

    # 余りを取る
    dp[i][k] %= mod

# SのN文字目までを使ってchokudaiの8文字目までを作る方法の数
print(dp[N][8])

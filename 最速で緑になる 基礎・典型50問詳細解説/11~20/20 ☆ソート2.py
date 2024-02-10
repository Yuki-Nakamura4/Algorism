# 入力の受け取り
N = int(input())
C = list(map(int, input().split()))

# mod=10^9+7と定義
mod = 10**9 + 7

# Cをソート
C.sort()

# 答えを格納する変数
ans = 1

# i=0~(N-1)まで
for i in range(N):
    # もしC[i]-i=0ならば
    if C[i] - i == 0:
        # 0を出力
        print(0)
        # 終了
        exit()

    # ansにC[i]-iをかける
    ans *= C[i] - i
    # 余りを取る。最後に余りを取るのではなく、計算の都度余りを取ることでTLEを防ぐ(モジュラ演算の分配法則)
    ans %= mod

# 答えを出力
print(ans)

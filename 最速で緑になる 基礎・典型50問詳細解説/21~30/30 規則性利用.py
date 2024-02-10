# 余りを定義
mod = 998244353

# 入力の受け取り
N = int(input())


# A~Bまでの和 等差数列の和の公式
# 引数：A,B→返り値：A~Bまでの和
def S(A, B):
    return (B - A + 1) * (A + B) // 2


# 答え
ans = 0

# x~1~18
for x in range(1, 19):
    # 10^x≤Nならば
    if 10**x <= N:
        # 「1~9*10**(x-1)までの和」
        ans += S(1, 9 * 10 ** (x - 1))
        # 余りを取る
        ans %= mod
    # 10^(x-1)≤N<10^xならば
    else:
        # 「1～(N-10^(x-1)+1)までの和」
        ans += S(1, N - 10 ** (x - 1) + 1)
        # 余りを取る
        ans %= mod
        # forを抜ける
        break

# 答えの出力
print(ans)

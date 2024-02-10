N = int(input())

A = list(map(int, input().split()))

ans = 0

for i in range(N):
    if A[i] <= 10:
        pass
    else:
        ans += A[i] - 10

print(ans)

# 別解
# 「A[i]が10より大きければ」 の部分を 「0か(A[i]-10)の大きい方」 と考えれば、
# ifを使わずにmaxで解くこともできる。

# 入力の受け取り
N = int(input())
A = list(map(int, input().split()))
# 答えの格納用変数
ans = 0
# xへAの値を順に入れる
for x in A:
    # 0と(x-10)の大きい方を足す
    ans += max(0, x - 10)
# 答えの出力
print(ans)

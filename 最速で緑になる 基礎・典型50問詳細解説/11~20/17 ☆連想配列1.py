from collections import defaultdict

N = int(input())
A = list(map(int, input().split()))

count = defaultdict(int) # 0で初期化された辞書

for i in range(N):
    count[A[i]] += 1

ans = N * (N - 1) // 2

# countの値(x)それぞれについて
for x in count.values():
    # Ai = Ajとなる組の数を引く
    ans -= x * (x - 1) // 2

print(ans)

# https://atcoder.jp/contests/abc206/tasks/abc206_c

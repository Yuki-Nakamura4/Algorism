N = int(input())

# X[d]: d日目から実行可能になるタスクのポイントを集めた配列
X = []
for i in range(0, N):
    X.append([])

for i in range(N):
    a, b = list(map(int, input().split()))
    X[a - 1].append(b)

# cnt[b]: b点のタスクの個数
# 点数の上限が100点なので、101要素の配列を用意しておく
cnt = [0] * 101
# ans: 得られるポイントの合計
ans = 0

# d日目について処理する
for d in range(N):
    # d日目から実行可能になるタスクをcntに追加する
    for b in X[d]:
        cnt[b] += 1

    # cnt[b] > 0である最大のbを探して加算する
    for b in range(100, 0, -1):
        if cnt[b] > 0:
            ans += b
            cnt[b] -= 1
            break
    print(ans)

# 貪欲法で解ける問題の多くは、"途中で「あえて最良でないものを選ぶ」ような選び方は、
# その選び方の一部分を変更することでより良い選び方か同等の選び方に必ず変形できる"ということを確認することで
# その正しさを証明できる。

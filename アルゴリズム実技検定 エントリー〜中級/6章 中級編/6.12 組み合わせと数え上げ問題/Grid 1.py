H, W = list(map(int, input().split()))
A = []
for i in range(H):
    s = input()
    A.append(s)

cnt = []
for i in range(H):
    cnt.append([0] * W)
# 初期条件。スタート地点の通り数は1
cnt[0][0] = 1

MOD = 10**9 + 7

for i in range(H):
    for j in range(W):
        # 壁マスならcnt[i][j]=0のままにする
        if A[i][j] == "#":
            continue
        # 左からの移動を考える場合
        if j > 0:
            cnt[i][j] += cnt[i][j - 1]
        if i > 0:
            cnt[i][j] += cnt[i - 1][j]
        cnt[i][j] %= MOD

print(cnt[H - 1][W - 1])

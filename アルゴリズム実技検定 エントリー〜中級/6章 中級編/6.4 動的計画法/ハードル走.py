N, L = list(map(int, input().split()))
X = list(map(int, input().split()))
T1, T2, T3 = list(map(int, input().split()))

# ハードルがある座標においてTrueとなるような配列
H = [False] * (L + 1)
for x in X:
    H[x] = True

# const[i]:座標iで行動を終了するまでの最小所要時間
# 非常に大きな値で初期化しておき、minを用いて更新する
cost = [float("inf")] * (L + 1)

# 初期条件
cost[0] = 0

for i in range(1, L + 1):
    # 行動1
    cost[i] = min(cost[i], cost[i - 1] + T1)
    # 行動2
    if i >= 2:
        cost[i] = min(cost[i], cost[i - 2] + T1 + T2)
    # 行動3
    if i >= 3:
        cost[i] = min(cost[i], cost[i - 4] + T1 + T2 * 3)
    # もしハードルがあれば加算
    if H[i]:
        cost[i] += T3

# 答えは座標Lでピッタリに止まるか、座標(L-3)〜(L-1)からジャンプ中にゴールしたもの
ans = cost[L]
for i in range(L - 3, L):
    if i >= 0:
        ans = min(ans, cost[i] + T1 // 2 + T2 * (2 * (L - i) - 1) // 2)

print(ans)

# グラフが大きい時の最短経路問題はダイクストラ法を使う
# 閉路が無かったら動的計画法でも良い

# ダイクストラ法は幅優先探索を一般化したもの
# コストがすべて1であれば幅優先探索と同じ

# 模範解答
import heapq

N = int(input())
g = [[] for _ in range(N + 1)]  # 隣接リスト g[i] = [(j, c)] iからjへコストcで移動可能
for i in range(1, N):
    A, B, X = map(int, input().split())
    g[i].append((i + 1, A))  # 一つ右隣のステージへコストAで移動できる
    g[i].append((X, B))  # ステージXへコストBで移動できる

INF = 10**18
d = [INF] * (N + 1)  # d[i] = ステージi開始するのにかかる最短時間 (INFで初期化)
d[1] = 0  # ステージ1をプレイするのにかかる時間は0

q = [(0, 1)]  # (最短開始時間, ステージ) ステージ1は最初からプレイ可能なので(0, 1)

while q:
    c, v = heapq.heappop(q)
    if d[v] < c:  # すでに最短時間が更新されていたらスキップ
        continue
    for u, w in g[v]:  # ステージuへコストwで移動できる
        if d[u] > d[v] + w:  # ステージuへの最短時間が更新できるなら更新
            d[u] = d[v] + w
            # ステージuへの最短時間が更新されたらヒープへ追加
            heapq.heappush(q, (d[u], u))
print(d[N] if d[N] < INF else -1)

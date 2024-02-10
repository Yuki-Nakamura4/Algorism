import heapq

N, M = map(int, input().split())

G = []
for _ in range(N):
    G.append([])

for _ in range(M):
    ai, bi = map(int, input().split())

    ai -= 1
    bi -= 1

    G[ai].append(bi)
    G[bi].append(ai)

# 頂点0から各頂点への最短距離を格納する配列
# N個の-1で満たしておく(-1は未訪問であることを表す)
dist = []
for _ in range(0, N):
    dist.append(-1)

# ダイクストラ法で使うヒープ
Q = []

# 始点となる頂点0をヒープに追加しておく
# (距離, 頂点)として追加する
heapq.heappush(Q, (0, 0))

# 始点となる頂点0への最短距離は0とする
dist[0] = 0

# ヒープから取り出したことがあるかを保存する配列
# 最初はN個のFalseで埋めておく
done = []
for _ in range(N):
    done.append(False)

# ダイクストラ法で各頂点への最短距離を求める
while len(Q) > 0:
    # ヒープの先頭の頂点を取り出してiとする
    d, i = heapq.heappop(Q)

    # もし前にヒープから取り出したことがあれば、
    # その頂点については処理済みとしてcontinueする
    if done[i]:
        continue

    # ヒープから頂点iを取り出したことを記録しておく
    done[i] = True

    # 頂点iに隣接する頂点を順番に見る
    # 見ている頂点をjとする
    for j in G[i]:
        # この問題では、辺の重みは常に1
        x = 1

        # 頂点jが未訪問だったとき、あるいは頂点jへの最短距離が更新可能だったとき、
        # 頂点jへの最短距離を更新して、ヒープの末尾に追加する
        if dist[j] == -1 or dist[j] > dist[i] + x:
            dist[j] = dist[i] + x
            heapq.heappush(Q, (dist[j], j))

if dist[N - 1] == 2:
    print("POSSIBLE")
else:
    print("IMPOSSIBLE")

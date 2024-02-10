import heapq

N, M = map(int, input().split())

# 隣接リストとしてグラフの情報を保持する配列
G = []
for _ in range(N):
    G.append([])

for _ in range(M):
    u, v, c = map(int, input().split())

    # uからvへと、重みcの辺が張られているため
    # 行き先のvだけでなく、重みのcも一緒に保存する
    G[u].append((v, c))
    G[v].append((u, c))

###################################
# プリム法で最小全域木問題を解く
##################################

# 頂点がマークされているかを格納する配列
# 頂点iがマークされているとき marked[i]=True となる
# 最初はどの頂点もマークされていないためN個のFalseで埋めておく
marked = []
for _ in range(N):
    marked.append(False)

# マークされている頂点の数を保持する変数
# 最初はどの頂点もマークされていないため0
# この値が0になったら終了する
marked_count = 0

# 最初に頂点0を選んでマークする
marked[0] = True
marked_count += 1

# 次に選ぶ辺の候補を入れるヒープ
Q = []

# 頂点0に隣接する辺を調べ、ヒープに入れる
for j, c in G[0]:
    # ヒープに選ぶ候補の辺を挿入する
    # (辺の重み, 頂点)として追加する
    heapq.heappush(Q, (c, j))

# 最小全域木の重みの合計を保存する変数
sum = 0

# すべての頂点がマークされるまで繰り返す
while marked_count < N:
    # ヒープから、最小の重みの辺を取り出す
    # これは(辺の重み、選んだ時にマークする頂点)の形式になっている
    c, i = heapq.heappop(Q)

    # 辺につながる頂点iがすでにマークされていたら、
    # この辺は失敗するのでスキップする
    if marked[i]:
        continue

    # 頂点iをマークする
    marked[i] = True
    marked_count += 1

    # 使った辺は最小全域木となるため、重みを保存しておく
    sum += c

    # 新たにマークした頂点iに隣接する辺を調べる
    for j, c in G[i]:
        # 辺がつなぐ頂点がすでにマークされていた場合はヒープに入れない
        if marked[j]:
            continue

        heapq.heappush(Q, (c, j))

# 最小全域木の重みの合計
print(sum)

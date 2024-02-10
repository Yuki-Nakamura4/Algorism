# 入力の受け取り
N, M = map(int, input().split())

# 道路の情報を格納する変数
connect = [[] for i in range(N + 1)]
# 道路の情報を受け取って格納
for i in range(M):
    A, B = map(int, input().split())
    connect[A].append(B)
    connect[B].append(A)

# 余りの定義
mod = 10**9 + 7

# まだ到達していない都市の移動時間(infinity：無限大)
# 大きめの数にする
inf = 10**15  # 10**15程度ならTLEしない

# (1)各都市の最短移動時間を記録するリストtimeを作る(初期値は大きな数)
time = [inf] * (N + 1)
# 都市①の最短移動時間は「0」
time[1] = 0

# (2)各都市にたどり着くまでの経路数を記録するリストcountを作る
count = [0] * (N + 1)
# 都市①に行く経路数は「1」
count[1] = 1

# (3)キューを用意
from collections import deque

que = deque()
# キューに都市①を入れる
que.append(1)

# (6)(4)~(5)をキューが空になるまで繰り返す
while 0 < len(que):
    # (4)キューの左端から要素(都市の番号)を取り出す(今いる街)
    now = que.popleft()

    # (5)今いる都市から行ける都市を確認する
    # nowから行ける都市を順にtoへ格納
    for to in connect[now]:
        # もし行ける都市の移動時間がinfならば(まだ更新されていない)
        if time[to] == inf:
            # (5-1)「経路数」=「今いる都市の経路数」
            count[to] = count[now]
            # (5-2)「最短移動時間」=「今いる都市の最短移動時間+1」
            time[to] = time[now] + 1
            # (5-3)キューに追加
            que.append(to)

        # そうでないなら(移動時間が更新済み)
        else:
            # 「最短移動時間」=「今いる都市の最短移動時間+1」(最短経路)ならば
            if (
                time[to] == time[now] + 1
            ):  # time[to]が真の最短経路じゃなかったら更新できなくない？て思ったけど幅優先探索だとそうはならない
                # (5-4)「経路数」+=「今いる都市の経路数」
                count[to] += count[now]

        # 余りを取る
        count[to] %= mod

# (7)答えを出力する
# Nが未到達であれば(「最短移動時間」が更新されていなければ)
if time[N] == inf:
    # たどり着けないため「0」を出力
    print(0)

# そうでないならば
else:
    # count[N]を出力
    print(count[N])

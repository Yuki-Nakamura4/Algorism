# 幅優先探索 → キューを使う
# ぜんぶ回りたいときに使う(木、迷路、グラフなど)

# 入力の受け取り
N, M = map(int, input().split())

# 道路の情報を格納するリスト
connect = [[] for i in range(N + 1)]

# M回受け取り
for i in range(M):
    # 入力の受け取り
    A, B = map(int, input().split())
    # connect[A]にBを追加
    # 都市1から都市2,3,4にいけるならconnect[1]=2,3,4
    connect[A].append(B)

# dequeをインポート
from collections import deque


# BFS
# 引数：スタート都市→返り値：スタート都市から行ける都市の数
def BFS(start):
    # 行ける都市を数える変数
    # スタート都市→スタート都市には必ず行けるから1
    count = 1

    # 訪問済み都市のリスト
    # 訪問済みならTrue、未訪問ならFalse
    visited = [False] * (N + 1)

    # スタート都市は訪問済みにする
    visited[start] = True

    # キューを用意
    que = deque()
    # キューへスタート都市を追加
    que.append(start)

    # キューが空になるまで
    while 0 < len(que):
        # 今いる都市
        now = que.popleft()

        # 今いる都市から行ける都市を順にtoへ
        for to in connect[now]:
            # もしtoが未訪問なら
            if visited[to] == False:
                # countにプラス1
                count += 1

                # toを訪問済みにする
                visited[to] = True

                # キューへtoを追加
                que.append(to)

    # 行ける都市の数を返す
    return count


# 答えを格納する変数
ans = 0

# x=1~N
for x in range(1, N + 1):
    # xをスタート地点としたときに行ける都市の数を順に足し算
    ans += BFS(x)

# 答えの出力
print(ans)

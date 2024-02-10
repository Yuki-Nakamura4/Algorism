# dequeは両端からappendとpopが可能なデータ構造
# メモリ効率がよく、どちらからもO(1)で操作できる
from collections import deque

# R行C列の迷路
R, C = list(map(int, input().split()))
# スタート地点の座標
sy, sx = list(map(int, input().split()))
# ゴール地点の座標
gy, gx = list(map(int, input().split()))

# 迷路の情報を受け取る
S = []

# R行の入力を受け取る
for i in range(R):
    s = input()
    S.append(s)

# 1始まりの入力を0始まりに直す
sy -= 1
sx -= 1
gx -= 1
gy -= 1

# 始点からの最小移動回数を管理する2次元配列。-1であれば未訪問であることを表す。
dist = []
for i in range(R):
    dist.append([-1] * C)

# キューを用意して、視点を入れる
Q = deque()
Q.append([sy, sx])
dist[sy][sx] = 0

# キューから取り出しながら探索する
while len(Q) > 0:
    i, j = Q.popleft()
    # 4つのマスを確認する
    for i2, j2 in [[i + 1, j], [i - 1, j], [i, j + 1], [i, j - 1]]:
        # もし盤面の範囲内でなければ無視する
        if not (0 <= i2 < R and 0 <= j2 < C):
            continue
        # もし壁マスであれば無視する
        if S[i2][j2] == "#":
            continue
        # もし未訪問(dist[i2][j2]が-1)であれば、距離を更新してキューに入れる
        if dist[i2][j2] == -1:
            dist[i2][j2] = dist[i][j] + 1
            Q.append([i2, j2])

# 視点から終点までの最小移動回数を出力する
print(dist[gy][gx])

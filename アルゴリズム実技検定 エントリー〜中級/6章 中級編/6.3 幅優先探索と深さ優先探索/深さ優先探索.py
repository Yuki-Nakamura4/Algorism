# 再帰上限を増やす
import sys

sys.setrecursionlimit(1000000)

# 入力
H, W = map(int, input().split())

S = []
for _ in range(H):
    s = input()
    S.append(s)

# 視点と終点の座標を探し、それぞれ(si, sj), (gi, gj)とする
for i in range(H):
    for j in range(W):
        if S[i][j] == "s":
            si, sj = i, j
        if S[i][j] == "g":
            gi, gj = i, j

# 訪問済みかどうかを管理する2次元配列
visited = []
for _ in range(H):
    visited.append([False] * W)


# 再帰関数dfsを定義する
def dfs(i, j):
    visited[i][j] = True
    # 4方向の隣マスを探索する
    for i2, j2 in [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]:
        # もし盤面の範囲内でなければ無視する
        if not (0 <= i2 < H and 0 <= j2 < W):
            continue
        # もし壁マスであれば無視する
        if S[i2][j2] == "#":
            continue
        # もしまだ見ていないマスであれば再帰的に呼び出す
        if not visited[i2][j2]:
            dfs(i2, j2)


# 始点から呼び出す
dfs(si, sj)

# 終点が訪問済みかどうかによってYesまたはNoを出力する
if visited[gi][gj]:
    print("Yes")
else:
    print("No")
